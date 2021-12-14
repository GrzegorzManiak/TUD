const fs = require('fs'),
    readline = require('readline');

const args:string[] = process.argv.slice(2),
    input:string = args[0];

if (input === undefined) 
    throw new Error('Missing input file');

    
let commentObject:any = {
    'color': 'This rule is used to specify the color of the text.',
    'background-color': 'This rule is used to specify the background color of the element.',
    'font-size': 'This rule is used to specify the font size of the text.',
    'font-family': 'This rule is used to specify the font family of the text.',
    'font-weight': 'This rule is used to specify the font weight of the text.',
    'font-style': 'This rule is used to specify the font style of the text.',
    'text-decoration': 'This rule is used to specify the text decoration of the text such as underline.',
    'text-align': 'This rule is used to specify the text alignment of the text.',
    'z-index': 'This rule is used to specify the z-index of the element.',
    'padding': 'This rule is used to specify the padding of the element.',
    'width': 'This rule is used to specify the width of the element.',
    'height': 'This rule is used to specify the height of the element.',
    'margin': 'This rule is used to specify the margin of the element.',
    'border': 'This rule is used to specify the border of the element.',
    'border-radius': 'This rule is used to specify the border radius of the element.',
    'border-width': 'This rule is used to specify the border width of the element.',
    'border-style': 'This rule is used to specify the border style of the element.',
    'border-color': 'This rule is used to specify the border color of the element.',
    'display': 'This rule is used to specify the display of the element.',
    'position': 'This rule is used to specify the position of the element.',
    'top': 'This rule is used to specify the top position of the element.',
    'left': 'This rule is used to specify the left position of the element.',
    'bottom': 'This rule is used to specify the bottom position of the element.',
    'right': 'This rule is used to specify the right position of the element.',
    'float': 'This rule is used to specify the float of the element.',
    'clear': 'This rule is used to specify the clear of the element.',
    'overflow': 'This rule is used to specify the overflow of the element.',
    'overflow-x': 'This rule is used to specify the overflow-x of the element.',
    'overflow-y': 'This rule is used to specify the overflow-y of the element.',
    'list-style': 'This rule is used to specify the list-style of the element.',
    'list-style-type': 'This rule is used to specify the list-style-type of the element.',
    'list-style-position': 'This rule is used to specify the list-style-position of the element.',
    'list-style-image': 'This rule is used to specify the list-style-image of the element.',
    'content': 'This rule is used to specify the content of the element.',
    'quotes': 'This rule is used to specify the quotes of the element.',
    'caption-side': 'This rule is used to specify the caption-side of the element.',
    'table-layout': 'This rule is used to specify the table-layout of the element.',
    'empty-cells': 'This rule is used to specify the empty-cells of the element.',
    'vertical-align': 'This rule is used to specify the vertical-align of the element.',
    'text-indent': 'This rule is used to specify the text-indent of the element.',
    'white-space': 'This rule is used to specify the white-space of the element.',
    'word-spacing': 'This rule is used to specify the word-spacing of the element.',
    'letter-spacing': 'This rule is used to specify the letter-spacing of the element.',
    'word-wrap': 'This rule is used to specify the word-wrap of the element.',
    'text-overflow': 'This rule is used to specify the text-overflow of the element.',
    'text-transform': 'This rule is used to specify the text-transform of the element.',
    'text-shadow': 'This rule is used to specify the text-shadow of the element.',
    'text-decoration-color': 'This rule is used to specify the text-decoration-color of the element.',
    'text-decoration-line': 'This rule is used to specify the text-decoration-line of the element.',
    'text-decoration-style': 'This rule is used to specify the text-decoration-style of the element.',
    'text-decoration-skip': 'This rule is used to specify the text-decoration-skip of the element.',
    'text-underline-position': 'This rule is used to specify the text-underline-position of the element.',
    'text-emphasis': 'This rule is used to specify the text-emphasis of the element.',
    'text-emphasis-color': 'This rule is used to specify the text-emphasis-color of the element.',
    'text-emphasis-style': 'This rule is used to specify the text-emphasis-style of the element.',
    'text-emphasis-position': 'This rule is used to specify the text-emphasis-position of the element.',
    'box-sizing': 'This rule is used to specify the box-sizing of the element.',
    'outline': 'This rule is used to specify the outline of the element.',
    'outline-color': 'This rule is used to specify the outline-color of the element.',
    'outline-style': 'This rule is used to specify the outline-style of the element.',
    'outline-width': 'This rule is used to specify the outline-width of the element.',
    'outline-offset': 'This rule is used to specify the outline-offset of the element.',
    'border-collapse': 'This rule is used to specify the border-collapse of the element.',
    'border-spacing': 'This rule is used to specify the border-spacing of the element.',
    'border-top': 'This rule is used to specify the border-top of the element.',
    'border-top-color': 'This rule is used to specify the border-top-color of the element.',
    'border-top-style': 'This rule is used to specify the border-top-style of the element.',
    'border-top-width': 'This rule is used to specify the border-top-width of the element.',
    'border-right': 'This rule is used to specify the border-right of the element.',
    'border-right-color': 'This rule is used to specify the border-right-color of the element.',
    'border-right-style': 'This rule is used to specify the border-right-style of the element.',
    'border-right-width': 'This rule is used to specify the border-right-width of the element.',
    'border-bottom': 'This rule is used to specify the border-bottom of the element.',
    'border-bottom-color': 'This rule is used to specify the border-bottom-color of the element.',
    'border-bottom-style': 'This rule is used to specify the border-bottom-style of the element.',
    'border-bottom-width': 'This rule is used to specify the border-bottom-width of the element.',
    'border-left': 'This rule is used to specify the border-left of the element.',
    'border-left-color': 'This rule is used to specify the border-left-color of the element.',
    'border-left-style': 'This rule is used to specify the border-left-style of the element.',
    'border-left-width': 'This rule is used to specify the border-left-width of the element.',
    'border-top-left-radius': 'This rule is used to specify the border-top-left-radius of the element.',
    'border-top-right-radius': 'This rule is used to specify the border-top-right-radius of the element.',
    'border-bottom-right-radius': 'This rule is used to specify the border-bottom-right-radius of the element.',
    'flex-direction': 'This rule is used to specify the flex-direction of the element.',
    'flex-wrap': 'This rule is used to specify the flex-wrap of the element.',
    'flex-flow': 'This rule is used to specify the flex-flow of the element.',
    'flex-grow': 'This rule is used to specify the flex-grow of the element.',
    'flex-shrink': 'This rule is used to specify the flex-shrink of the element.',
    'flex-basis': 'This rule is used to specify the flex-basis of the element.',
    'flex': 'This rule is used to specify the flex of the element.',
    'order': 'This rule is used to specify the order of the element.',
    'align-content': 'This rule is used to specify the align-content of the element.',
    'align-items': 'This rule is used to specify the align-items of the element.',
    'align-self': 'This rule is used to specify the align-self of the element.',
    'justify-content': 'This rule is used to specify the justify-content of the element.',
    'justify-items': 'This rule is used to specify the justify-items of the element.',
    'justify-self': 'This rule is used to specify the justify-self of the element.',
    'grid-template-columns': 'This rule is used to specify the grid-template-columns of the element.',
    'grid-template-rows': 'This rule is used to specify the grid-template-rows of the element.',
    'grid-template-areas': 'This rule is used to specify the grid-template-areas of the element.',
    'grid-auto-columns': 'This rule is used to specify the grid-auto-columns of the element.',
    'grid-auto-rows': 'This rule is used to specify the grid-auto-rows of the element.',
    'grid-auto-flow': 'This rule is used to specify the grid-auto-flow of the element.',
    'grid-column-start': 'This rule is used to specify the grid-column-start of the element.',
    'grid-column-end': 'This rule is used to specify the grid-column-end of the element.',
    'grid-row-start': 'This rule is used to specify the grid-row-start of the element.',
    'grid-row-end': 'This rule is used to specify the grid-row-end of the element.',
    'grid-column': 'This rule is used to specify the grid-column of the element.',
    'grid-row': 'This rule is used to specify the grid-row of the element.',
    'grid-area': 'This rule is used to specify the grid-area of the element.',
    'grid-column-gap': 'This rule is used to specify the grid-column-gap of the element.',
    'grid-row-gap': 'This rule is used to specify the grid-row-gap of the element.',
    'grid-template': 'This rule is used to specify the grid-template of the element.',
    'grid': 'This rule is used to specify the grid of the element.',
    'background': 'This rule is used to specify the background of the element.',
    'gap': 'This rule is used to specify the gap of the element.',
    'margin-left': 'This rule is used to specify the margin-left of the element.',
    'margin-right': 'This rule is used to specify the margin-right of the element.',
    'padding-right': 'This rule is used to specify the padding-right of the element.',
    'padding-left': 'This rule is used to specify the padding-left of the element.',
    'max-width': 'This rule is used to specify the max-width of the element.',
}

function comment(str:string):string {
    let split:string[] = str.split(':'),
        tag:string = split[0].toLowerCase().trim();
    
    if(commentObject[tag] == undefined) return '';
    return commentObject[tag];
}

async function read(str:string):Promise<string> {
    return new Promise((resolve, reject) => {
        let output:string = '';

        let rl = readline.createInterface({
            input: fs.createReadStream(str)
        });

        rl.on('line', (line:string) => {
            let com:string = comment(line);

            if(com == '') return output += `${line}\n`;
            else return output += `/* ${com} */\n   ${line}\n`;
        });

        rl.on('close', () => {
            resolve(output);
        });
        
        rl.on('error', (err:any) => {
            reject(err);
        });
    });
}

(async() => {
    console.log('Starting...');

    let content:string = await read(input),
        output:string = `./css.fixex.css`;

    console.log('Writing...');
    
    //write to file
    fs.writeFile(output, content, (err:any) => {
        if(err) throw err;
    });

    console.log('Done!');
})();