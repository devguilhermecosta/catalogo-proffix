"use strict";

// modal before open
let imgModal = document.querySelector('#C-modal_defaul_img');
const images = document.querySelectorAll('.C-detail_gallery_img');

images.forEach((img) => {
    img.addEventListener("click", () => {
        let path = img.getAttribute('src');
        imgModal.setAttribute('src', path);
    })
})


// modal after open
const defaultImg = document.querySelector('#C-modal_defaul_img');
const defaulContainerImg = document.querySelector('.C-detail_c_img');
const modal = document.querySelector('.C-modal');
const modalImg = document.querySelector('.C-modal_modal-img');
const allImages = document.querySelectorAll('.C-detail_gallery_img');
const buttonRight = document.querySelector('#C-modal_button-right');
const buttonLeft = document.querySelector('#C-modal_button-left');
const buttonCloseModal = document.querySelector('#C-modal_close');

(() => {
    const imagesLenght = allImages.length;
    let count = 0;

    defaulContainerImg.addEventListener("click", () => {
        const path = defaultImg.getAttribute('src');
        modalImg.setAttribute('src', path);
        modal.classList.toggle('is_disabled');
        modal.classList.toggle('modal-open');
        count = 0;
    });

    buttonCloseModal.addEventListener("click", () => {
        modal.classList.toggle('is_disabled');
        modal.classList.toggle('modal-open');
    })
    
    buttonRight.addEventListener("click", () => {
        if (count < imagesLenght) {
            try {
                let path = allImages[count + 1].getAttribute('src');
                count++;
                modalImg.setAttribute('src', path);
            } catch(e) {e};
        }
    
    })
    
    buttonLeft.addEventListener("click", () => {
        if (count > 0 ) {
            try {
                let path = allImages[count-1].getAttribute('src');
                count--;
                modalImg.setAttribute('src', path);
            } catch(e) {e};
        }
    })
})()