"use strict";

let imgModal = document.querySelector('#img-modal');
const images = document.querySelectorAll('.C-detail_gallery_img');

images.forEach((img) => {
    img.addEventListener("click", () => {
        let path = img.getAttribute('src');
        imgModal.setAttribute('src', path);
    })
})