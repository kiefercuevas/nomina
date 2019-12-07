
let btnAddTransaction = document.querySelector("#btnAdd")
    .addEventListener("click", ExecuteAddTransaction)

let btnSubmit = document.querySelector("#btnSubmit")
    .addEventListener("click", SaveAsientoContable)


async function ExecuteAddTransaction() {

    const table = document.querySelector("#crearAsientoTable");
    let newTrElement = document.createElement("TR");
    let empleados = [];
    let ingresosDeducciones = [];
    let newTdElement = null;

    await fetch('/Empleados/getEmpleados')
        .then(res => res.json())
        .then(data => empleados = data.empleados)

    await fetch("/Ingresos/getIngresos")
        .then(res => res.json())
        .then(data => data.ingresos.forEach(d => {
            d.tipo = Object.keys(data).indexOf('deducciones') > -1 ? 'deducion' : 'ingreso';
            ingresosDeducciones.push(d);
        }))

    await fetch("/Deduciones/getDeduciones")
        .then(res => res.json())
        .then(data => data.deducciones.forEach(d => {
            d.tipo = Object.keys(data).indexOf('deducciones') > -1 ? 'deducion' : 'ingreso';
            ingresosDeducciones.push(d);
        }));

    let TdSelectEmpleado = `<select class='form-control'>${empleados.map((e) => `<option value='${e.id}'>${e.Nombre}</option>`).join(" ")}`;
    let TdInputMonto = `<input class='form-control transacionMonto' type='number' min='0' value='0' />`;

    let TdSelectIngresoDeduccion = `<select class='form-control'>${ingresosDeducciones.map((c) => `<option value='${c.id}' data-tipo='${c.tipo}' data-dependeSalario='${c.DependeSalario}'>${c.Nombre}</option>`).join(" ")}`;

    for (let child of [TdSelectEmpleado, TdSelectIngresoDeduccion, TdInputMonto]) {
        let newTd = document.createElement("TD");
        newTd.innerHTML = child;
        newTrElement.appendChild(newTd);
    }
    table.appendChild(newTrElement);
}


async function SaveAsientoContable() {

    const selectMoneda = document.getElementById('IDMoneda');
    let selectMonedaOptions = selectMoneda.options;
    const descripcion = document.getElementById("Descripcion").value;

    const JsonAsientoContable = {
        IDauxiliar: parseInt(document.getElementById("IDauxiliar").value),
        Moneda: selectMonedaOptions[selectMonedaOptions.selectedIndex].value,
        Transacciones: [],
        DebitoTotal: 0,
        CreditoTotal: 0,
    }

    const table = document.querySelector("#crearAsientoTable");
    let trs = table.getElementsByTagName('tr');

    if (trs.length < 1) {
        alert("Debe ingresar al menos una transaccion");
        return;
    }

    for (tr of trs) {
        let tds = tr.getElementsByTagName('td');

        let EmpOption = tds[0].firstChild.options;
        let monto = tds[tds.length - 1].firstChild.value;
        let ingresoDeduccion = tds[1].firstChild.options;
        let selectedIngresoDeduccion = ingresoDeduccion[ingresoDeduccion.selectedIndex];
        let dependeSalario = selectedIngresoDeduccion.getAttribute('data-dependesalario')

        console.log(dependeSalario);
        monto = monto.length == 0 ? 0 : parseFloat(monto);

        if (dependeSalario == "true" && parseInt(monto) > 100) {
            alert("El ingreso/deduccion depende del salario por lo que debe ser un porcentaje del 1%-100%")
            return;
        }

        let newTransaction = {
            Empleado: parseInt(EmpOption[EmpOption.selectedIndex].value),
            Monto: monto,
            Descripcion: descripcion,
            IdIngresoDeduccion: ingresoDeduccion[ingresoDeduccion.selectedIndex].value,
            Tipo: selectedIngresoDeduccion.getAttribute('data-tipo'),
            DependeSalario: dependeSalario == "true" ? true : false,
        }

        JsonAsientoContable.Transacciones.push(newTransaction);
    }

    fetch('create', {
        method: 'POST',
        body: JSON.stringify(JsonAsientoContable),
    })
        .then(res => res.json())
        .then(data => {
            if (data.status == 200) {
                alert(data.mensaje);
                location.href = '/Transacciones';
            } else {
                alert(data.mensaje);
            }
        })

}


