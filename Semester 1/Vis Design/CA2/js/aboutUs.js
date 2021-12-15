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