function defineShortcut(dom, key2) {
    dom = document.getElementById(dom);
    //add and event listner when a key is pressed
    document.addEventListener('keydown', async function(e) {
        //if the control key is pressed and the seccond key is pressed
        if (e.ctrlKey && e.code == key2) {
            dom.className = 'shortcutBox shortcutBoxActive';
            await sleep(1000);
            dom.className = 'shortcutBox';
        }
    });

}