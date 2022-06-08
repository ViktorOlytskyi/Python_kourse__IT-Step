// const table = document.getElementById("table-div")
// console.log(table);
// console.log(table.children[0].children[0].innerText);
// console.log(table.children[0]);


const findTable = document.querySelector('.table-div table tbody');
const findRableTH = document.querySelectorAll('.table-div th');
const arrayPeople = 
[
    {
        name: 'Mark',
        lastName: 'Zuckerberg',
        age: 34,
        company: 'Facebook'
    },
    {
        name: 'Larry',
        lastName: 'Page',
        age: 45,
        company: 'Google'
    },
    {
        name: 'Timothy',
        lastName: 'Cook',
        age: 57,
        company: 'Apple'
    },
    {
        name: 'Bill',
        lastName: 'Gates',
        age: 62,
        company: 'Microsoft'
    },
]

const arrayPeopleClone = arrayPeople;
const createElementTD = document.createElement('td');

function deleteСells(){
    const findCells = document.querySelectorAll('.table-div td').forEach(item => item.remove());
}

function sortByFirstName(array){
    deleteСells();

    array.sort((a, b) => a.name > b.name ? 1 : -1);

    createRowsTable(array);
}

function sortByLastName(array){
    deleteСells();

    array.sort((a, b) => a.lastName > b.lastName ? 1 : -1);

    createRowsTable(array);
}

function sortByAge(array){
    deleteСells();

    array.sort((a, b) => a.age > b.age ? 1 : -1);

    createRowsTable(array);
}

function sortByCompany(array){
    deleteСells();

    array.sort((a, b) => a.company > b.company ? 1 : -1);

    createRowsTable(array);
}

function createRowsTable(array){
    for(let i = 0; i < array.length; i++){
        const createRowTable = document.createElement('tr');
        
        for(item in arrayPeople[i]){
            const cloneElementTD = createElementTD.cloneNode(false);
            cloneElementTD.innerHTML = arrayPeople[i][item];
            createRowTable.append(cloneElementTD);
        }

        findTable.append(createRowTable);
    }
}

findTable.addEventListener('click', e => {
    if(e.target.nodeName === 'TH'){
        if(e.target.innerText === 'Firstname'){
            sortByFirstName(arrayPeopleClone);
        } else if(e.target.innerText === 'Lastname'){
            sortByLastName(arrayPeopleClone);
        } else if(e.target.innerText === 'Age'){
            sortByAge(arrayPeopleClone);
        } else if(e.target.innerText === 'Company'){
            sortByCompany(arrayPeopleClone);
        }
    }
});

createRowsTable(arrayPeopleClone);