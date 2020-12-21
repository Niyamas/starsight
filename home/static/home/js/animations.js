class Animations {

    constructor() {

    }

    static nav() {
        /**
         * Adds transition classes to the navbar after scrolling 70 units.
         * Will remove these classes once the user scrolls back to the top.
         */

        console.log('Running Animations.nav()')

        const nav = document.getElementById('nav')
        const navStarsight = document.getElementById('navStarsight')
        const navLinks = Array.from( document.getElementsByClassName('nav__links__link') )

        window.addEventListener('scroll', () => {
            //console.log('scrollY = ', window.scrollY)

            if (window.scrollY > 70) {

                nav.classList.add('sticky')
                navStarsight.classList.add('sticky')

                navLinks.forEach( (link) => {

                    link.classList.add('sticky')
                })
            }
            else {

                nav.classList.remove('sticky')
                navStarsight.classList.remove('sticky')

                navLinks.forEach( (link) => {

                    link.classList.remove('sticky')
                })
            }
        })
    }

}

Animations.nav()