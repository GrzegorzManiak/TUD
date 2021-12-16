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