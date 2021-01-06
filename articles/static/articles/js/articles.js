class Articles {

    constructor() {

        this.articleTotalNumber = undefined
    }

    static async getArticlesAll() {
        /**
         * Used in getArticles().
         * 
         * Fetch request to the API to get a list of all
         * articles and display them in /articles.
         * 
         * http://localhost:8000/api/v2/pages/?type=articles.ArticleDetailPage&fields=_,id,title,banner_text,topic,image,html_url,first_published_at&topic=Stars&order=-first_published_at&limit=6
         */
        console.log('Fetching all articles...')

        // Fetch all articles
        let url = 'http://localhost:8000/api/v2/pages/?type=articles.ArticleDetailPage&fields=_,id,title,banner_text,topic,image,html_url,first_published_at&order=-first_published_at&limit=6'
        await fetch(url)
        .then( (response) => response.json() )
        .then( (articleList) => {

            let articleInfo = ''
            let months = {
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

            // Store the total number of articles
            this.articleTotalNumber = articleList['meta']['total_count']

            // Store the list of articles
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
                else {
                    articleTopic = article['topic'].toUpperCase()
                }

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

            // Call the pagination generation here
            console.log('Number of articles:', this.articleTotalNumber)
        })

    }

    static async getArticlesTopic(topic) {
        /**
         * Used in getArticles().
         * 
         * When a topic (not all) is clicked, it will
         * fetch all the articles and display them.
         */
        console.log('topic clicked:', topic.dataset.topic_id, topic.dataset.topic_name)

        let APIFilterTopic = `&topic=${topic.dataset.topic_id}`
        let url = `http://localhost:8000/api/v2/pages/?type=articles.ArticleDetailPage&fields=_,id,title,banner_text,topic,image,html_url,first_published_at&order=-first_published_at&limit=6`
        url += APIFilterTopic

        fetch(url)
        .then( (response) => response.json() )
        .then( (articleList) => {

            let articleInfo = ''
            let months = {
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

            // Store the total number of articles
            this.articleTotalNumber = articleList['meta']['total_count']

            // Store the list of articles
            articleList = articleList['items']

            articleList.forEach( (article) => {

                // Convert first_publsihed_at date to long date format.
                let date = new Date(article['meta']['first_published_at'])
                let firstPublishedAt = months[date.getMonth()] + ' ' + date.getDate() + ', ' + date.getFullYear()

                // If the topic is null, return an empty string intead of null.
                let articleTopic = article['topic']
                if (articleTopic === null) {

                    articleTopic = ''
                }
                else {

                    articleTopic = article['topic'].toUpperCase()
                }

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

            // Call the pagination generation here
            console.log('Number of articles:', this.articleTotalNumber)
        })
        
    }

    static topicTransitions(topic) {
        /**
         * Add class "clicked" that animates the topic background & color
         * transitions and removes the transitions in its sibling list elements.
         */

        topic.classList.add('clicked')
        for (let sibling of topicsAll.parentNode.children) {

            if (sibling !== topic) {
                sibling.classList.remove('clicked')
            }
        }
    }

    static async getArticles() {
        /**
         * 
         */
        let topicsAll = document.getElementById('topicsAll')
        let topics = Array.from( document.getElementsByClassName('topics__topic--topic') )

        // Highlight "All" topic on page load
        topicsAll.classList.add('clicked')

        // Get all articles on page load
        this.getArticlesAll()

        // When the user clicks "All", gets all the articles and displays them
        // Also applies background & color transition on topic click.
        topicsAll.addEventListener('click', () => {

            this.getArticlesAll()
            this.topicTransitions(topicsAll)
        })

        // For each non-all topic clicked, fetch the respective articles.
        // Also applies background & color transition on topic click.
        topics.forEach( (topic) => {

            topic.addEventListener('click', () => {

                this.getArticlesTopic(topic)
                this.topicTransitions(topic)
            })
        })

    }

}

Articles.getArticles()