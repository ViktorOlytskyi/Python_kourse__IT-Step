
var arr=document.getElementById("list").children;


for (let i = 0; i < arr.length; i++) {
        if(arr[i].innerHTML.substring(0,4)==="http")
    {
        console.log(arr[i].innerHTML);
        arr[i].style.cssText="text-decoration: underline dashed red;"
    }
    
        
}

