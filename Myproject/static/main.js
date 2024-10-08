document.addEventListener("DOMContentLoaded", function() {
    const totalWorkItems = document.querySelectorAll(".work-item").length;
    let index = 0;

    // Preloader
    window.addEventListener("load", function() {
        document.querySelector(".preloader").classList.add("loaded");
    });

    // Navigation Toggle
    document.querySelector(".nav-toggle").addEventListener("click", function() {
        const nav = document.querySelector(".header .nav");
        if (nav.style.maxHeight) {
            nav.style.maxHeight = null;
            nav.style.opacity = 0;
        } else {
            nav.style.maxHeight = nav.scrollHeight + "px";
            nav.style.opacity = 1;
        }
    });

    // Close navigation on link click for mobile
    document.querySelectorAll(".header .nav a").forEach(link => {
        link.addEventListener("click", function() {
            if (window.innerWidth < 768) {
                const nav = document.querySelector(".header .nav");
                nav.style.maxHeight = null;
                nav.style.opacity = 0;
            }
        });
    });

    // Sticky Header
    window.addEventListener("scroll", function() {
        const header = document.querySelector(".header");
        if (window.scrollY > 100) {
            header.classList.add("fixed");
        } else {
            header.classList.remove("fixed");
        }
    });

    // Smooth Scrolling
    document.querySelectorAll("a").forEach(anchor => {
        anchor.addEventListener("click", function(event) {
            if (this.hash !== "") {
                event.preventDefault();
                const hash = this.hash;
                document.querySelector(hash).scrollIntoView({
                    behavior: 'smooth'
                });
                history.pushState(null, null, hash);
            }
        });
    });

    // // Set lightbox image max-height
    // function setLightboxImgHeight() {
    //     const wHeight = window.innerHeight;
    //     document.querySelector(".lightbox-img").style.maxHeight = wHeight + "px";
    // }
    // setLightboxImgHeight();
    // window.addEventListener("resize", setLightboxImgHeight);

    // // Lightbox functionality
    // document.querySelectorAll(".work-item-inner").forEach(item => {
    //     item.addEventListener("click", function() {
    //         index = Array.from(document.querySelectorAll(".work-item")).indexOf(this.parentElement);
    //         document.querySelector(".lightbox").classList.add("open");
    //         lightboxSlideShow();
    //     });
    // });

    // document.querySelector(".lightbox .prev").addEventListener("click", function() {
    //     index = (index === 0) ? totalWorkItems - 1 : index - 1;
    //     lightboxSlideShow();
    // });

    // document.querySelector(".lightbox .next").addEventListener("click", function() {
    //     index = (index === totalWorkItems - 1) ? 0 : index + 1;
    //     lightboxSlideShow();
    // });

    // document.querySelector(".lightbox-close").addEventListener("click", function() {
    //     document.querySelector(".lightbox").classList.remove("open");
    // });

    // document.querySelector(".lightbox").addEventListener("click", function(event) {
    //     if (event.target.classList.contains("lightbox")) {
    //         this.classList.remove("open");
    //     }
    // });

    // function lightboxSlideShow() {
    //     const workItems = document.querySelectorAll(".work-item");
    //     const imgSrc = workItems[index].querySelector("img").getAttribute("data-large");
    //     const category = workItems[index].querySelector("h4").innerHTML;
    //     document.querySelector(".lightbox-img").setAttribute("src", imgSrc);
    //     document.querySelector(".lightbox-category").innerHTML = category;
    //     document.querySelector(".lightbox-counter").innerHTML = `${index + 1} / ${totalWorkItems}`;
    // }

    // Dialog functionality
    document.querySelector("#button").addEventListener("click", function() {
        const dialog = document.querySelector("#dialog");
        dialog.style.display = "block";
        // Simple dialog box implementation
        dialog.addEventListener("click", function(event) {
            if (event.target === this) {
                this.style.display = "none";
            }
        });
    });
});

const dropdownMenu = document.querySelector(".dropdown-menu");
const dropdownButton = document.querySelector(".dropdown-button");

if (dropdownButton) {
  dropdownButton.addEventListener("click", () => {
    dropdownMenu.classList.toggle("show");
  });
}

// Upload Image
const photoInput = document.querySelector("#avatar");
const photoPreview = document.querySelector("#preview-avatar");
if (photoInput)
  photoInput.onchange = () => {
    const [file] = photoInput.files;
    if (file) {
      photoPreview.src = URL.createObjectURL(file);
    }
  };

// Scroll to Bottom
const conversationThread = document.querySelector(".room__box");
if (conversationThread) conversationThread.scrollTop = conversationThread.scrollHeight;

var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("openModal");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
btn.onclick = function() {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// JavaScript to dynamically adjust the blur based on text length
document.addEventListener('DOMContentLoaded', function () {
    const messageContainer = document.getElementById('message-container');
    
    // Get the length of the message body
    const messageLength = messageContainer.innerText.length;
  
    // Adjust the blur effect based on the message length
    const blurAmount = Math.min(30, Math.max(10, messageLength * 0.1)); // Change the formula as needed
  
    // Set the new backdrop-filter blur value
    messageContainer.style.backdropFilter = `blur(${blurAmount}px)`;
  });
  