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

            // Store HTML image for APOD
            let apodHTML = `
                <h2>Astronomy Picture of the Day</h2>
                <h3>${apod.title}</h3>
                <p>${apod.date}</p>
                <img src="${apod.hdurl}" alt="NASA's Astronomy Picture of the Day (APOD)"></img>
                <p>${apod.explanation}</p>
            `

            // Place apodHTML in innerHTML of div with ID='apod'
            document.getElementById('apod').innerHTML = apodHTML

        })
    }
}

ExternalAPIS.getAPOD()