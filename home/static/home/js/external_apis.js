class ExternalAPIS {

    constructor() {

    }

    static async getAPODs() {
        /**
         * 
         */
        let url = 'https://api.nasa.gov/planetary/apod?api_key=' + nasaAPIKey
        await fetch(url)
        .then( (response) => response.json() )
        .then( (apod) => {

            console.log(`apod data structure = ${apod}`)

            // Store HTML image for APOD
            let apodHTML = `
                <h2 class="apod__banner">
                    Astronomy Picture of the Day
                    <span class="apod__date">${apod.date}</span>
                </h2>
                <a href="https://apod.nasa.gov/apod/astropix.html" target="_blank">
                    <img class="apod__img" src="${apod.url}" alt="NASA's Astronomy Picture of the Day (APOD)"></img>
                </a>
                <h3>
                    ${apod.title}
                    <span class="apod__copyright">by ${apod.copyright}</span>
                </h3>
                <p class="apod__description">
                    ${apod.explanation}
                    <a class="apod__description__fade" href="#"></a>
                </p>
                <div class="apod__read-more">Read more</div>
            `

            // Place apodHTML in innerHTML of div with ID='apod'
            document.getElementById('apod').innerHTML = apodHTML

        })
    }

    static APODError(response) {
        /**
         * 
         */
        if (!response.ok) {
            throw Error(response.statusText)
        }
        return response;
    }


    static async getAPOD() {
        /**
         * 
         */
        let url = 'https://api.nasa.gov/planetary/apod?api_key=' + nasaAPIKey
        await fetch(url)
        .then( (response) => {

            // If no API errors, proceed to the next promise
            if (response.ok) {
                return response
            }

            let date = new Date()
            let dateTimeNow = ( date.getMonth() + 1) + '-' + date.getDate() + '-' + date.getFullYear()

            // Store HTML image for APOD
            let apodHTML = `
                <h2 class="apod__banner">
                    Astronomy Picture of the Day
                    <span class="apod__date">(updating) ${dateTimeNow}</span>
                </h2>
                <a href="#">
                    <img class="apod__img" src="${defaultAPOD}" alt=""></img>
                </a>
                <h3>
                    Cloud Belts of Jupter
                    <span class="apod__copyright">by NASA's Juno Space Probe</span>
                </h3>
                <p class="apod__description">
                    NASA is in the midst of updating their Astronomy Picture of the Day.
                    Here's a picture of a pearlescent Jupiter taken by Juno—high above and safe
                    from the powerful storms of Jupiter!
                 </p>
            `

            // Place apodHTML in innerHTML of div with ID='apod'
            document.getElementById('apod').innerHTML = apodHTML

            // Stop .then promises
            throw Error(response.statusText)

        })
        .then( (response) => response.json() )
        .then( (apod) => {

            console.log(`apod data structure = ${apod}`)

            // Store HTML image for APOD
            let apodHTML = `
                <h2 class="apod__banner">
                    Astronomy Picture of the Day
                    <span class="apod__date">${apod.date}</span>
                </h2>
                <a href="https://apod.nasa.gov/apod/astropix.html" target="_blank">
                    <img class="apod__img" src="${apod.url}" alt="NASA's Astronomy Picture of the Day (APOD)"></img>
                </a>
                <h3>
                    ${apod.title}
                    <span class="apod__copyright">by ${apod.copyright}</span>
                </h3>
                <p class="apod__description">
                    ${apod.explanation}
                    <a class="apod__description__fade" href="#"></a>
                </p>
                <div class="apod__read-more">Read more</div>
            `

            // Place apodHTML in innerHTML of div with ID='apod'
            document.getElementById('apod').innerHTML = apodHTML

        })
    }
}

ExternalAPIS.getAPOD()