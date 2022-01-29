const pages = {
    'home': './home.html',
    'tips': './tips.html',
    'css': './css.html',
    'html': './html.html',
    'about us': './aboutus.html',
    'survey': './survey.html'
}

const imgs = {
    'gregoria': {
        img: './imgs/aboutus/greg1.png',
        elem: undefined,
        name: 'Gregoria',
        bio: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, laboris nisi ut aliquip ex ea commodo consequat.'
    },
    'grzegorz': {
        img: './imgs/aboutus/greg5.png',
        elem: undefined,
        name: 'Grzegorz',
        bio: 'Hey, my name is Grzegorz Maniak, I\'m studying computing at TU Tallaght campus, I have a great interest in web and software development, I also enjoy the outdoors, I love to travel, camp and hike.'
    },
    'gregor': {
        img: './imgs/aboutus/greg2.png',
        elem: undefined,
        name: 'Gregor',
        bio: 'Ello, my name is Gregor, I\'m studying computing at TU Tallaght campus, I have a great interest in web and software development, I also enjoy the outdoors, I love to travel, camp and hike.'
    },
    'grock': {
        img: './imgs/aboutus/greg4.png',
        elem: undefined,
        name: 'Grock',
        bio: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, laboris nisi ut aliquip ex ea commodo consequat.'
    },
    'grebama': {
        img: './imgs/aboutus/greg3.png',
        elem: undefined,
        name: 'Grebama',
        bio: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, laboris nisi ut aliquip ex ea commodo consequat.'
    },
}

let curentlyAnimating = false,
    currentPageName,
    scrollPos,
    height,
    stack = [];

//
// GENERAL FUNCTIONS
//

function remToPx(rem) {
    let styles = getComputedStyle(document.documentElement);
    //all rem is, is the root font size of the HTML document, which is generally 16px.
    //this means, all we have to do is get the font size of the HTML document,
    //multiply it by the rem value, and we have the px value.

    //we have to parse the value of the font size, because it is a string.
    //returned as '16px', formating it returns it as a 16.
    return parseFloat(styles.fontSize) * rem;
}

// Really basic sleep function.
function sleep(ms) {
    // Create a new promise, no rejection as this cant fail
    return new Promise((resolve) => {
        // Time out for some ammount of time,
        // once done exec resolve(), resolving the promise.
        setTimeout(resolve, ms);
    })
}


function hamburger(id) {
    let hamburgerBtn = document.getElementById(id),
        navLogo = document.getElementById('navLogo'),
        hamburgerContent = document.getElementById('hamburgerContent');

    hamburgerBtn.addEventListener('click', () => {
        switch (hamburgerBtn.checked) {
            case true:
                hamburgerContent.className = hamburgerContent.className.replace('hamburgerContentInvisible', '');
                hamburgerContent.className += ' hamburgerContentVisible';

                document.documentElement.className = 'htmlStopScroll';
                navLogo.classList.replace('logoColorMenuClosed', 'logoColorMenuOpen');
                break;

            case false:
                hamburgerContent.className = hamburgerContent.className.replace('hamburgerContentVisible', '');
                hamburgerContent.className += ' hamburgerContentInvisible';

                document.documentElement.className = '';
                navLogo.classList.replace('logoColorMenuOpen', 'logoColorMenuClosed');
                break;
        }
    });

    document.documentElement.className = '';
}

// adds elements to the nav bar from the 'pages' object.
function addElements(navID, selected, urlParams = '') {
    // Get the navbar element
    let element = document.getElementById(navID);

    // For each item in the Pages object
    Object.keys(pages).forEach((key) => {
        // create a bew LI element and a new P element
        let li = document.createElement('li'),
            p = document.createElement('p');

        // Assign the LI an ID
        li.class = key;

        // Assign the P its text content
        p.textContent = key;

        // Adds an event listner, eg when this element is clicked
        li.addEventListener('click', async(elm) => {
            // delaying the execution of the function,
            // active so that the animation has time to finish.
            await sleep(200);

            // if the user is trying to get, eg, from home => home, dont refresh
            if (currentPageName != key)
                document.location = `${pages[key]}?${urlParams}`;
        });

        if (currentPageName == key) p.className = selected;

        li.appendChild(p);
        element.appendChild(li)
    });
}

function selectPageIndicator(num) {
    // get the elements inside the 'pageIndicator' element
    let elements = [...document.getElementsByClassName('pageIndicatorElement')];
    // convert it from a Dom collection to an array

    elements.forEach((elm, i) => {
        if (i == num && i < elements.length) elm.className = 'pageIndicatorElement pageIndicatorElementActive';
        else elm.className = 'pageIndicatorElement';
        i++;
    });
}

async function startScroll() {
    let prevPos = -1,
        currentPage = 0,
        notScrolledFor = 0;

    while (true) {
        // Get the current scroll position  
        scrollPos = document.scrollingElement.scrollTop;
        height = document.documentElement.clientHeight;

        await sleep(5);
        let closerToPage = Math.round(scroll / height),
            moveTo = closerToPage * height

        if (scroll != moveTo) {
            await sleep(1);
            notScrolledFor++;

            if (notScrolledFor > 100) {
                window.scrollTo(0, moveTo);
                notScrolledFor = 0;
            }
        }

        if (scrollPos == prevPos) continue;
        else notScrolledFor = 0;

        currentPage = Math.round(scrollPos / height);
        selectPageIndicator(currentPage);

        prevPos = scrollPos;
    }
}

//Carousel
function addCarouselItems() {
    let carousel = document.getElementById('carousel');
    carousel.className = 'carouselVisable';

    Object.keys(imgs).forEach((key, i) => {
        //create the parent element for this img, heading and bio
        let div = document.createElement('div');

        //add text to the div
        div.innerHTML = `<img class='carouselImg' src="${imgs[key].img}" alt="${imgs[key].name}"><p class='carouselText'><span class='carouselText'>${imgs[key].name},</span> ${imgs[key].bio}</p>`;

        //give the div a name
        div.name = key;

        switch (i) {
            case 0: // Image on the left hand side
                div.className = 'scaleOutToLeft';
                div.id = 'carouselLeft';
                break;

            case 1: // Image in the middle
                div.className = 'carouselSelected';
                div.id = 'carouselCenter';
                div.getElementsByTagName('img')[0].useMap = '#aboutus';
                break;

            case 2: // Image on the right hand side
                div.className = 'scaleOutToRight';
                div.id = 'carouselRight';
                break;

            default:
                // Since this image wont be seen, add it to the stack
                stack = [div, ...stack];
                // and make it invisable
                div.className = 'invisible';
                break;
        }

        imgs[key].elem = div;
        carousel.appendChild(div);

        div.onclick = () => carouselScroll(div);
    });
}

async function carouselScroll(elem, from = '') {
    if (curentlyAnimating === true)
        return;

    curentlyAnimating = true;

    //This is the element currently in the middle of the carousel
    let cs = document.getElementById('carouselCenter');
    cs.getElementsByTagName('img')[0].useMap = '';

    let left = document.getElementById('carouselLeft'), // Gets the left most image
        right = document.getElementById('carouselRight'); // Gets the right most image

    //If the image from the left is clicked
    if (elem.id == 'carouselLeft') {
        //Aimate the image to scale in from the left hand side to the middle
        elem.className = 'scaleInFromLeft';

        //set 'from' to left since the user clicked on the left most img
        from = 'Left';
    }

    //If the image from the right is clicked
    if (elem.id == 'carouselRight') {
        //Aimate the image to scale in from the right hand side to the middle
        elem.className = 'scaleInFromRight';

        //set 'from' to right since the user clicked on the right most img
        from = 'Right';
    }

    //The image that just got clicked is now in the middle
    elem.id = 'carouselCenter';
    elem.getElementsByTagName('img')[0].useMap = '#aboutus';

    //Move the center image in the correct direction
    switch (from) {
        case 'Left': //move the img to the right
            //If theres an image to the right, move it behind the center
            if (right) {
                right.id = '';
                right.className = 'moveCenterFromRight'; //animate the move
                stack = [...stack, right]; //add the img to the left side of the stack
            }

            if (!document.getElementById('carouselLeft')) {
                stack[0].className = 'moveLeftFromCenter'; //animate the move
                stack[0].id = 'carouselLeft'; //lable the imgs position
                stack.shift(); //remove the img from the stack
            }

            cs.id = 'carouselRight'; //lable the imgs position
            cs.className = 'scaleOutToRight'; //animate the move

            break;

        case 'Right': // move the img to the left
            //If theres an image to the left, move it behind the center
            if (left) {
                left.id = '';
                left.className = 'moveCenterFromLeft'; //animate the move
                stack = [left, ...stack]; //add the img to the right side of the stack
            }

            if (!document.getElementById('carouselRight')) {
                stack[stack.length - 1].className = 'moveRightFromCenter'; //animate the move
                stack[stack.length - 1].id = 'carouselRight'; //lable the imgs position
                stack.pop(); //remove the img from the stack
            }

            cs.id = 'carouselLeft'; //lable the imgs position
            cs.className = 'scaleOutToLeft'; //animate the move

            break;
    }

    //Wait for the animations to finish, they take 2 seconds
    await sleep(1700);
    return curentlyAnimating = false;
}

function carousel(side) {
    switch (side) {
        case 'left':
            return carouselScroll(document.getElementById('carouselLeft'));

        case 'right':
            return carouselScroll(document.getElementById('carouselRight'));
    }
}

async function addVisualizer(dom, targetTag, style = '') {
    dom = document.getElementById(dom);

    let children = [...dom.children],
        inputs = [...children[0].children],
        output = children[1].children[0];

    function focus(num) {
        inputs.forEach((input, i) => {
            if (i == num) input.className = 'inputInteractiveFocus';
            else input.className = '';
        });
    }

    inputs.forEach((input, i) => {
        function change() {
            focus(i);
            output.style.cssText = input.value + ';' + style;
        }

        input.addEventListener('focus', () => change());

        input.addEventListener('input', () => change());

        if (i == 0) change();
    });
}

async function headingExample(dom, text) {
    dom = document.getElementById(dom);

    let children = [...dom.children],
        buttons = [...children[0].children],
        output = children[1].children[0];

    function focus(num) {
        buttons.forEach((button, i) => {
            if (i == num) button.className = 'headingButtonActive';
            else button.className = '';
        });
    }

    buttons.forEach((button, i) => {
        function change() {
            focus(i);
            let tag = button.textContent.replace(/[<>]/g, '');
            output.innerHTML = `<${tag}>${text}</${tag}><span class='codeTag'>&lt;${tag}&gt;</span>${text}<span class='codeTag'>&lt;/${tag}&gt;</span>`;
        }

        button.addEventListener('click', () => {
            change();
        });

        if (i == 0) change();
    });
}

async function listExample(dom) {
    dom = document.getElementById(dom);

    let children = [...dom.children],
        buttons = [...children[0].children],
        output = children[1].children[0];

    function focus(num) {
        buttons.forEach((button, i) => {
            if (i == num) button.className = 'headingButtonActive';
            else button.className = '';
        });
    }

    buttons.forEach((button, i) => {
        function change(listTo = 'orderd list') {
            focus(i);

            switch (button.textContent) {
                case 'orderd list':
                    listTo = 'ol';
                    break;

                case 'unorderd list':
                    listTo = 'ul';
                    break;
            }

            output.innerHTML = `<${listTo} class='codeList'> <li>item 1</li> <li>item 2</li> <li>item 3</li> </${listTo}><span class='codeTag'>&lt;${listTo}&gt;</span><br><span class='codeTag codePaddingLeft'>&lt;li&gt;</span>item 1<span class='codeTag'>&lt;/li&gt;</span><br><span class='codeTag codePaddingLeft'>&lt;li&gt;</span>item 2<span class='codeTag'>&lt;/li&gt;</span><br><span class='codeTag codePaddingLeft'>&lt;li&gt;</span>item 3<span class='codeTag'>&lt;/li&gt;</span><br><span class='codeTag'>&lt;${listTo}&gt;</span>`;
        }

        button.addEventListener('click', () => {
            change();
        });

        if (i == 0) change();
    });
}

async function imgExample(dom) {
    dom = document.getElementById(dom);

    let children = [...dom.children],
        buttons = [...children[0].children],
        output = children[1];

    function focus(num) {
        buttons.forEach((button, i) => {
            if (i == num) button.className = 'headingButtonActive';
            else button.className = '';
        });
    }

    buttons.forEach((button, i) => {
        function change() {
            focus(i);
            output.innerHTML = button.value;
        }

        button.addEventListener('click', () => {
            change();
        });

        if (i == 0) change();
    });
}

async function titleExample(dom) {
    dom = document.getElementById(dom);
    dom.addEventListener('input', () => {
        if (dom.value.trim() == '') document.title = 'Html | Group 17';
        else document.title = dom.value;
    });
}

async function navPos() {
    let previosScrollPos = undefined;

    while (true) {
        //Slow down the loop down a little, saves on resources
        await sleep(1);

        //get the current scroll position
        let scrollPos = window.scrollY;

        //check if the user has scrollPos, if not, dont continue
        if (previosScrollPos === scrollPos)
            continue;

        //get the document styles
        let styles = getComputedStyle(document.documentElement),
            navBar = document.getElementsByTagName('nav')[0], // get the nav bar element
            headerHeight = parseFloat(styles.getPropertyValue('--header-height')); // get the header height

        //convert the nav bar height to px from rem
        let headerHeightPX = remToPx(headerHeight);

        //if the user scrolled past the header, change its class
        if (scrollPos > headerHeightPX - (headerHeightPX * 0.8)) {
            navBar.classList.add("belowHeader");
            navBar.classList.remove("overHeader");
        } else {
            navBar.classList.add("overHeader");
            navBar.classList.remove("belowHeader");
        }

        //set the previous scroll position to the current scroll position
        previosScrollPos = scrollPos;
    }
}

//creates a shorcut
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

function createOTP(dom, ammount, callback = (inputs) => {}, inputRegex = /[0-9]/) {
    let element = document.getElementById(dom),
        inputs = [];

    function focus(input) {
        inputs.forEach((key, i) => {
            if (i === input)
                key.focus();
        });
    }

    for (let i = 0; i < ammount; i++) {
        let input = document.createElement('input');

        input.setAttribute('maxlength', '1')
        input.setAttribute('class', 'tfaInputBox');
        input.setAttribute('id', 'tfaInputBox' + i);

        element.appendChild(input);
        inputs.push(input);

        input.onkeydown = function(inputKey) {
            switch (inputKey.key) {
                case 'Backspace': //backspace
                    input.value = '';
                    focus(inputs.indexOf(input) - 1);
                    break;

                case 'Enter': //enter
                    callback(inputs);
                    break;

                default: //any other key
                    // check if the keypressed conforms to the regular expression, 
                    // and its not loger than one character, eg if they pressed CapsLock
                    if (inputRegex.test(inputKey.key.trim() || inputKey.key.length > 1) !== true)
                        break;

                    focus(inputs.indexOf(input) + 1);
                    input.value = inputKey.key;
                    break;
            }

            return false;
        }
    }
}