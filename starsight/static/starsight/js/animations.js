class Animations {

    constructor() {

    }

    static nav() {
        /**
         * Adds transition classes to the navbar after scrolling 70 units.
         * Will remove these classes once the user scrolls back to the top.
         */

        //console.log('Running Animations.nav()')

        let nav = document.getElementById('nav')
        let navStarsight = document.getElementById('navStarsight')
        let navLinks = Array.from( document.getElementsByClassName('nav__links__link') )

        let navLinkFirst = Array.from( document.getElementsByClassName('nav__links__li') )[0]

        let navHamHouse = document.getElementById('navHamHouse')
        let navHamburgerTop = document.getElementById('navHamburgerTop')
        let navHamburgerBottom = document.getElementById('navHamburgerBottom')

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
                navHamburgerTop.classList.add('sticky')
                navHamburgerBottom.classList.add('sticky')
            }
            else {

                nav.classList.remove('sticky')
                navStarsight.classList.remove('sticky')

                navLinks.forEach( (link) => {

                    link.classList.remove('sticky')
                })

                navLinkFirst.classList.remove('sticky')
                navHamHouse.classList.remove('sticky')
                navHamburgerTop.classList.remove('sticky')
                navHamburgerBottom.classList.remove('sticky')

                // ***Add classList.remove() to the ul & li elements
            }
        })
    }

    static mobileMenu() {
        /**
         * Animates the mobile menu by toggling "open" classes
         * when the user interacts with it. Applicable for viewports
         * that are less than 1250 pixels in width.
         */

        let navHamHouse = document.getElementById('navHamHouse')
        let navHamburger = document.getElementById('navHamburger')
        let navHamburgerTop = document.getElementById('navHamburgerTop')
        let navHamburgerBottom = document.getElementById('navHamburgerBottom')

        let navLinks = document.getElementById('navLinks')
        let navLink = Array.from( document.getElementsByClassName('nav__links__li') )

        // Opens the mobile menu when clicking on the ham house icon.
        navHamHouse.addEventListener('click', () => {

            navHamHouse.classList.toggle('open')
            navHamburger.classList.toggle('open')
            navHamburgerTop.classList.toggle('open')
            navHamburgerBottom.classList.toggle('open')
            navLinks.classList.toggle('open')

            navLink.forEach( (link) => {

                link.classList.toggle('open')
            })
        })

        // Adds an event listener to the document that evaluates each
        // click and if it clicked outside of the mobile menu, it will
        // remove all the mobile menu "open" classes, effectively closing
        // the menu.
        // See: https://stackoverflow.com/questions/14188654/detect-click-outside-element-vanilla-javascript
        document.addEventListener('click', (event) => {

            let navLinksClick = navLinks.contains(event.target)
            let navHamHouseClick = navHamHouse.contains(event.target)

            if (!navLinksClick && !navHamHouseClick) {

                navHamHouse.classList.remove('open')
                navHamburger.classList.remove('open')
                navHamburgerTop.classList.remove('open')
                navHamburgerBottom.classList.remove('open')
                navLinks.classList.remove('open')
    
                navLink.forEach( (link) => {
    
                    link.classList.remove('open')
                })
            }
        })

    }

}

Animations.nav()
Animations.mobileMenu()