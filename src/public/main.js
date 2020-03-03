




window.addEventListener('load', function() {
    console.log('All assets are loaded')
})




function IsJsonString(str) {
    try {
        JSON.parse(str);
    } catch (e) {
        return false;
    }
    return true;
}



