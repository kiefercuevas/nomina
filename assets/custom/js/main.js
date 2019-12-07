
async function RegisterAsiento(){
    
    let selectedCheckbox = document.querySelectorAll('input[type=checkbox]:checked');
    let transactionIds = [];

    if(selectedCheckbox.length == 0){
        alert("Debe seleccionar al menos una transaccion");
        return;
    }

    for(let checkbox of selectedCheckbox){
        transactionIds.push(checkbox.getAttribute('data-id'));
    }


    await fetch('RegistrarTransaccion', {
        method: 'POST',
        body: JSON.stringify({transactionIds}),
      })
      .then(res => res.json())
      .then(data => {
          if(data.status == 200){
              let result = confirm("Esta seguro de que desea registrar estas transacciones?")
              if(result){

                //ENVIANDO AL SERVICIO WEB
                fetch('https://apecaccountingapi.azurewebsites.net/api/account-entry', 
                        {
                            method: 'POST',
                            body: JSON.stringify(data.Asiento),
                            headers: { 
                                'Accept': 'application/json',
                                'Content-Type': 'application/json' 
                            },
                        }
                    ).then(res => res.json())
                    .then(data => {
                        alert(`Se registraran las transacciones con el ID ${data.debitEntryId}`);

                        //Registrando las transacciones
                        fetch('RegistrarIdTransacciones', {
                            method: 'POST',
                            body: JSON.stringify({transactionIds,"IDtransacionRegistrada":data.debitEntryId}),
                          })
                          .then(res => res.json())
                          .then(data => {
                              if(data.status == 200){
                                 alert(data.message);
                                 location.reload();
                              }
                                
                          })
                          .catch(err => alert(`Ha ocurrido un error ${err}`))


                    })
                    .catch(err => alert(`Ha ocurrido un error ${err}`))

              }
          }else{
              alert(`Ha ocurrido un error ${data.message}`);
          }
      })
      .catch(err => alert(`Ha ocurrido un error ${err}`))
}



function SelectAllUncheckedTransaction(){
    let notSelectedCheckbox = document.querySelectorAll('input[type=checkbox]:not(:checked)');

    for(checkbox of notSelectedCheckbox){
        checkbox.checked = true;
    }
}

function RemoveSelectAllUncheckedTransaction(){
    let notSelectedCheckbox = document.querySelectorAll('input[type=checkbox]:checked');

    for(checkbox of notSelectedCheckbox){
        checkbox.checked = false;
    }
}