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