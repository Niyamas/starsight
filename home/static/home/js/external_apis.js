class ExternalAPIS {

    constructor() {

    }

    static async getAPOD() {
        /**
         * 
         */
        let url = 'https://api.nasa.gov/planetary/apod?api_key=' + nasaAPIKey
        await fetch(url)
        .then( (response) => response.json() )
        .then( (apod) => {

            console.log(`apod data structure = ${apod}`)

            let descriptionFirst = apod.explanation.substring(0, 300)
            let descriptionSecond = apod.explanation.substring(300)

            // Store HTML image for APOD
            /* let apodHTML = `
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
                <p class="apod__description">${apod.explanation}</p>
            ` */
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