class Articles {

    constructor() {

    }

    static async getArticlesAll() {
        /**
         * Fetch request to the API to get a list of all
         * articles and display them in /articles.
         */
        console.log('Running Articles.getArticlesAll()')

        let url = 'http://localhost:8000/api/v2/pages/?type=articles.ArticleDetailPage&fields=_,id,title,banner_text,topic,image,html_url,first_published_at&order=-first_published_at&limit=6'
        await fetch(url)
        .then( (response) => response.json() )
        .then( (articleList) => {

            let articleInfo = ''
            const months = {
                0: 'January',
                1: 'February',
                2: 'March',
                3: 'April',
                4: 'May',
                5: 'June',
                6: 'July',
                7: 'August',
                8: 'September',
                9: 'October',
                10: 'November',
                11: 'December',
            }

            articleList = articleList['items']

            articleList.forEach( (article) => {
                
                //console.log(article['meta']['first_published_at'])

                // Convert first_publsihed_at date to long date format.
                let date = new Date(article['meta']['first_published_at'])
                let firstPublishedAt = months[date.getMonth()] + ' ' + date.getDate() + ', ' + date.getFullYear()

                // If the topic is null, return an empty string intead of null.
                let articleTopic = article['topic']
                if (articleTopic === null) {

                    articleTopic = ''
                }

                console.log('image url: ', article['image']['meta']['detail_url'])

                articleInfo += `
                    <article class="article">
                        <a href="${article['meta']['html_url']}">
                            <img class="article__img" src="${article['image']['meta']['download_url']}" alt="">
                        </a>
                
                        <div class="article__content">
                            <h2 class="article__content__title"><a href="#">${article['title']}</a></h2>
                
                            <a class="article__content__topic" href="#">${articleTopic}</a>
                            <span class="article__content__date">${firstPublishedAt}</span>
                
                            <a class="article__content__text" href="#">${article['banner_text']}</a>
                        </div>
                    </article>
                `

                document.getElementById('listings').innerHTML = articleInfo

            })
        })

    }
}

Articles.getArticlesAll()