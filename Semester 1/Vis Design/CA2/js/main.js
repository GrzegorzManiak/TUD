const pages = {
    'home': './index.html',
    'ui/ux': './uxui.html'
}

let currentPageName;

// Really basic sleep function.
function sleep(ms){
    // Create a new promise, no rejection as this cant fail
    return new Promise((resolve) => {
        // Time out for some ammount of time,
        // once done exec resolve(), resolving the promise.
        setTimeout(resolve, ms);
    })
}

function currentPage(page) {
    currentPageName = page;
}

// adds elements to the nav bar from the 'pages' object.
function addElements(navID, selected){
    // Get the navbar element
    let element = document.getElementById(navID);

    // For each item in the Pages object
    Object.keys(pages).forEach((key) => {
        // create a bew LI element and a new P element
        let li = document.createElement('li'),
            p = document.createElement('p');
        
        // Assign the LI an ID
        li.id = key;

        // Assign the P its text content
        p.textContent = key;
        
        // Adds an event listner, eg when this element is clicked
        li.addEventListener('click', async(elm) => {
            // Im delaying the page change to let clicking transform finish
            await sleep(200);

            // if the user is trying to get, eg, from home => home, dont refresh
            if(currentPageName != key) document.location = pages[key];
        });

        if(currentPageName == key) li.className = selected;
    
        li.appendChild(p);
        element.appendChild(li)
    });
}