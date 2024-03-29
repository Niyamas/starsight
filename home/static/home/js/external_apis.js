class ExternalAPIS {

    constructor() {

    }

    static addReadMoreAnimation() {
        /**
         * Adds click event listeners to the APOD
         * read more button and the APOD white text fade.
         * On click, will animate the description box to
         * open.
         */

        const readMore = document.getElementById('readMore')
        const descriptionFade = document.getElementById('descriptionFade')
        const description = document.getElementById('description')

        readMore.addEventListener('click', () => {

            // Toggle between "Read more" and "Show less" when clicking the read more button
            if (readMore.innerHTML === 'Read more') {
                
                readMore.innerHTML = 'Show less'
            }
            else {

                readMore.innerHTML = 'Read more'
            }

            description.classList.toggle('apod__description--animation')
            descriptionFade.classList.toggle('apod__description__fade--animation')
        })

        // Toggle between "Read more" and "Show less" when clicking the faded text
        descriptionFade.addEventListener('click', () => {

            // Toggle between "Read more" and "Show less" when clicked.
            if (readMore.innerHTML === 'Read more') {
                
                readMore.innerHTML = 'Show less'
            }
            else {

                readMore.innerHTML = 'Read more'
            }

            description.classList.toggle('apod__description--animation')
            descriptionFade.classList.toggle('apod__description__fade--animation')
        })


        // Change read more button to cooler-green on button hover
        readMore.addEventListener('mouseover', () => {

            // cooler-green
            readMore.style.color = '#5de4e4'
        })

        // Change read more button back to cool-green on button hover out
        readMore.addEventListener('mouseout', () => {

            // cool-green
            readMore.style.color = '#4FC0C0'
        })

        // Change read more button to cooler-green on fade hover
        descriptionFade.addEventListener('mouseover', () => {

            // cooler-green
            readMore.style.color = '#5de4e4'
        })

        // Change read more button back to cool-green on fade hover out
        descriptionFade.addEventListener('mouseout', () => {

            // cool-green
            readMore.style.color = '#4FC0C0'
        })

    }

    static async getAPOD() {
        /**
         * Fetchs NASA's Astronomy Picture of the Day
         * and its attributes. Outputs to the home page
         * sidebar.
         */

        let url = 'https://api.nasa.gov/planetary/apod?api_key=' + nasaAPIKey
        await fetch(url)
        .then( (response) => {

            // If no API errors, proceed to the next promise (i.e. .then)
            if (response.ok) {
                return response
            }

            let date = new Date()

            let options = { year:'numeric', month:'long', day:'numeric' }
            let dateTimeNow = date.toLocaleDateString('en-US', options)


            let apodHTML

            if (defaultAPODURL === 'None') {

                // @todo: add the animation and readmore stuff when using default APOD

                // Store HTML image for APOD if the URL set in Wagtail is not defined.
                // To style Wagtail's rich text, need to place text within a div.
                // In the CSS, call the rich text like so: "classname.p {}".
                apodHTML = `
                    <h3 class="apod__banner">ASTRONOMY PICTURE OF THE DAY</h3>

                    <a href="https://apod.nasa.gov/apod/astropix.html" target="_blank">
                        <img class="apod__img" src="${defaultAPOD}" alt=""></img>
                    </a>

                    <h3 class="apod__title">
                        <a href="https://apod.nasa.gov/apod/astropix.html" target="_blank">
                            ${defaultAPODTitle}
                        </a>
                    </h3>

                    <span class="apod__copyright">by ${defaultAPODCredits}&nbsp;</span>

                    <span class="apod__date">${dateTimeNow}</span>

                    <div class="apod__description">${defaultAPODText}</div>
                `
            }
            else {

                // Store HTML image for APOD if there is a URL set in Wagtail
                apodHTML = `
                    <h3 class="apod__banner">ASTRONOMY PICTURE OF THE DAY</h3>

                    <a href="${defaultAPODURL}" target="_blank">
                        <img class="apod__img" src="${defaultAPOD}" alt=""></img>
                    </a>

                    <h3 class="apod__title">
                        <a href="${defaultAPODURL}" target="_blank">
                            ${defaultAPODTitle}
                        </a>
                    </h3>

                    <span class="apod__copyright">by ${defaultAPODCredits}&nbsp;</span>

                    <span class="apod__date">${dateTimeNow}</span>

                    <div class="apod__description">${defaultAPODText}</div>
                `
            }

            // Place apodHTML in innerHTML of div with ID='apod'
            document.getElementById('apod').innerHTML = apodHTML

            // Stop .then promises
            throw Error(response.statusText)

        })
        .then( (response) => response.json() )
        .then( (apod) => {

            //console.log(`apod data structure = ${apod}`)

            // Store HTML image for APOD
            let apodHTML

            // Boolean check if apod.url is an embedded youtube link.
            let apodYTCheck = apod.url.includes('https://www.youtube.com/')
            //console.log('includes:', apodYTCheck)

            let apodDate = new Date(apod.date)
            let options = { year:'numeric', month:'long', day:'numeric' }
            let apodDateFormatted = apodDate.toLocaleDateString('en-US', options)

            // If APOD description is > 276 characters and it's not a YouTube link, add blur and read more button.
            // Also outputs either an img or iframe tag depending if the apod.url is an image or an embedded YouTube
            // video.
            if (apod.explanation.length > 276 && apodYTCheck === false) {

                apodHTML = `
                    <h3 class="apod__banner">ASTRONOMY PICTURE OF THE DAY</h3>

                    <a href="https://apod.nasa.gov/apod/astropix.html" target="_blank">
                        <img class="apod__img" src="${apod.url}" alt="NASA's Astronomy Picture of the Day (APOD)"></img>
                    </a>

                    <h3 class="apod__title">${apod.title}</h3>

                    <span class="apod__copyright">by ${apod.copyright}&nbsp;</span>

                    <span class="apod__date">${apodDateFormatted}</span>

                    <p id="description" class="apod__description">
                        ${apod.explanation}
                        <span id="descriptionFade" class="apod__description__fade"></span>
                    </p>

                    <div id="readMore" class="apod__read-more">Read more</div>
                `
            }
            else if (apod.explanation.length <= 276 && apodYTCheck === false) {

                apodHTML = `
                    <h3 class="apod__banner">ASTRONOMY PICTURE OF THE DAY</h3>

                    <a href="https://apod.nasa.gov/apod/astropix.html" target="_blank">
                        <img class="apod__img" src="${apod.url}" alt="NASA's Astronomy Picture of the Day (APOD)"></img>
                    </a>

                    <h3 class="apod__title">${apod.title}</h3>

                    <span class="apod__copyright">by ${apod.copyright}&nbsp;</span>

                    <span class="apod__date">${apodDateFormatted}</span>

                    <p class="apod__description">${apod.explanation}</p>
                `
            }
            else if (apod.explanation.length > 276 && apodYTCheck === true) {
                // @todo: is picture-in-picture right syntax?
                apodHTML = `
                    <h3 class="apod__banner">ASTRONOMY PICTURE OF THE DAY</h3>

                    <iframe class="apod__iframe" src="${apod.url}" frameborder="0" picture-in-picture allowfullscreen></iframe>

                    <h3 class="apod__title">${apod.title}</h3>

                    <span class="apod__copyright">by ${apod.copyright}&nbsp;</span>

                    <span class="apod__date">${apodDateFormatted}</span>

                    <p id="description" class="apod__description">
                        ${apod.explanation}
                        <span id="descriptionFade" class="apod__description__fade"></span>
                    </p>

                    <div id="readMore" class="apod__read-more">Read more</div>
                `
            }
            else if (apod.explanation.length <= 276 && apodYTCheck === true) {

                apodHTML = `
                    <h3 class="apod__banner">ASTRONOMY PICTURE OF THE DAY</h3>

                    <iframe class="apod__iframe" src="${apod.url}" frameborder="0" picture-in-picture allowfullscreen></iframe>

                    <h3 class="apod__title">${apod.title}</h3>

                    <span class="apod__copyright">by ${apod.copyright}&nbsp;</span>

                    <span class="apod__date">${apodDateFormatted}</span>
                    
                    <p class="apod__description">${apod.explanation}</p>
                `
            }

            //console.log(`apod.url = ${apod.url}`)

            // Place apodHTML in innerHTML of div with ID='apod'
            document.getElementById('apod').innerHTML = apodHTML

            // Add read more event listener on click to expand the APOD description
            this.addReadMoreAnimation()
        })
    }

    static async getCNEOS() {
        /**
         * https://ssd-api.jpl.nasa.gov/doc/cad.html
         * 
         * Currently, there are no comets that will be less than 0.05 au
         * in the next 60 days, but keep checking. Wait to build the comet
         * watch graph widget.
         */

        //let url = 'https://ssd-api.jpl.nasa.gov/cad.api?api_key=' + nasaAPIKey
        let url = 'https://ssd-api.jpl.nasa.gov/cad.api?comet=true'
        await fetch(url)
        .then( (response) => response.json() )
        .then( (CAD) => {

            console.log('CAD', CAD)
        })
    }

}

ExternalAPIS.getAPOD()
ExternalAPIS.getCNEOS()