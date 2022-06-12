// function check(){
//     var check = document.getElementsByClassName("checkboxes") 
//     for (var i=0, max=check.length; i < max; i++) {
        
//         // if (check[i].checked){
//         //     document.getElementsByClassName(check[i].value)[0].style.display = "block"
//         // }else{
//         //     document.getElementsByClassName(check[i].value)[0].style.display = "none"
//         // }
//     }
    
// }
var showingadd = false
var showingdelete = false
function show(){
    showingadd = !showingadd
    if (showingadd){
        document.querySelector(".addCat").style.display = "flex"
    }else{
        document.querySelector(".addCat").style.display = "none"
    }
}
document.getElementById("addBtn").addEventListener("click", show)

function showDelete(){
    showingdelete = !showingdelete
    if (showingdelete){
        document.querySelector(".deleteCat").style.display = "block"
    }else{
        document.querySelector(".deleteCat").style.display = "none"
    }
    
}
document.getElementById("deleteBtn").addEventListener("click", showDelete)
