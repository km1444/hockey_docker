const table = document.querySelector('table');
let colIndex = -1
table.onclick = function(e) {
    if(e.target.tagName != 'TH') return
    let th = e.target
    sortTable(th.cellIndex, th.getAttribute('data-type'), colIndex === th.cellIndex)
    colIndex = (colIndex === th.cellIndex) ? -1 : th.cellIndex;
};

function sortTable(colNum, type, isSorted) {
    let tbody = table.querySelector('tbody')
    for (let elem of table.querySelectorAll('.table-warning')) {
        elem.removeAttribute("class")
    }
    let rowsArray = Array.from(tbody.rows)
    let compare;
    switch(type) {
        case 'number':
            compare = function(rowA, rowB) {
                rowA.cells[colNum].setAttribute('class', "table-warning");
                rowB.cells[colNum].setAttribute('class', "table-warning");
                return rowB.cells[colNum].innerHTML - rowA.cells[colNum].innerHTML
            }
            break;
        case 'string':
            compare = function(rowA, rowB) {
                return rowA.cells[colNum].innerText > rowB.cells[colNum].innerText ? 1 : -1
            }
            break;
    }
    if (isSorted) rowsArray.sort(compare).reverse()
        else rowsArray.sort(compare)
    
    tbody.append(...rowsArray)
}
