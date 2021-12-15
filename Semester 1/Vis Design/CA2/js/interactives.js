async function addVisualizer(dom, targetTag) {
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
            output.style.cssText = input.value;
        }

        input.addEventListener('focus', () => change());

        input.addEventListener('input', () => change());
    });

    focus(0);
    output.style.cssText = inputs[0].value;
}