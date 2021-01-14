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
         * 
         */

        let navHamHouse = document.getElementById('navHamHouse')
        let navHamburger = document.getElementById('navHamburger')
        let navHamburgerTop = document.getElementById('navHamburgerTop')
        let navHamburgerBottom = document.getElementById('navHamburgerBottom')

        let navLinks = document.getElementById('navLinks')
        let navLink = Array.from( document.getElementsByClassName('nav__links__li') )

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
    }

}

Animations.nav()
Animations.mobileMenu()