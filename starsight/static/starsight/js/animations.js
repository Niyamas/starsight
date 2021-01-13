class Animations {

    constructor() {

    }

    static nav() {
        /**
         * Adds transition classes to the navbar after scrolling 70 units.
         * Will remove these classes once the user scrolls back to the top.
         */

        //console.log('Running Animations.nav()')

        const nav = document.getElementById('nav')
        const navStarsight = document.getElementById('navStarsight')
        const navLinks = Array.from( document.getElementsByClassName('nav__links__link') )

        const navLinkFirst = Array.from( document.getElementsByClassName('nav__links__li') )[0]
        const navHamHouse = document.getElementById('navHamHouse')
        //let navHamburgerBefore = getComputedStyle(document.getElementById('navHamburger'), '::before').getPropertyValue('transform')

        

        window.addEventListener('scroll', () => {
            //console.log('scrollY = ', window.scrollY)

            if (window.scrollY > 70) {

                //console.log('navHamburgerBefore=', navHamburgerBefore)

                nav.classList.add('sticky')
                navStarsight.classList.add('sticky')

                navLinks.forEach( (link) => {

                    link.classList.add('sticky')
                })

                navLinkFirst.classList.add('sticky')
                navHamHouse.classList.add('sticky')
            }
            else {

                nav.classList.remove('sticky')
                navStarsight.classList.remove('sticky')

                navLinks.forEach( (link) => {

                    link.classList.remove('sticky')
                })

                navLinkFirst.classList.remove('sticky')
                navHamHouse.classList.remove('sticky')
            }
        })
    }

}

Animations.nav()