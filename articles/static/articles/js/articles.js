class Articles {

    constructor() {

        // Article variables
        this.articleTotalNumber = undefined
        this.currentTopic = undefined
        this.currentTopicID = undefined

        // Pagination variables
        this.currentPageNumber = 1
        this.articleQuotient = undefined
        this.articleRemainder = undefined
    }

    static async fetchArticles(url) {
        /**
         * 
         */
        await fetch(url)
        .then( (response) => response.json() )
        .then( (articleList) => {

            // Store the total number of articles (used in pagination)
            this.articleTotalNumber = articleList['meta']['total_count']

            // For adding to the article listings innerHTML
            let articleHTML = ''

            // If zero articles are fetched, add a notice to the HTML,
            // and if there are, fetch the articles from the given url.
            if (this.articleTotalNumber === 0) {

                console.log('no articles')

                articleHTML = `
                    <div>There are no articles for this topic.</div>
                `

                document.getElementById('listings').innerHTML = articleHTML
            }
            else {

                
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
    
                    articleHTML += `
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
    
                    document.getElementById('listings').innerHTML = articleHTML
    
                })
    
                // Call the pagination generation here where this.articleTotalNumber is successfully updated
                this.createPagination()
            }

        })
    }

    static createPagination() {
        /**
         * 
         */
        this.articleQuotient = Math.floor(this.articleTotalNumber / 6)       // Number of pages (6 articles per page)
        this.articleRemainder = this.articleTotalNumber % 6                  // If multiples of 6 can't be reached, will show remainder of articles in the last page
        let paginationHTML = ``

        //console.log('this.articleQuotient=', this.articleQuotient, 'this.articleRemainder=', this.articleRemainder)

        // If there are more than 6 articles and there are a remainder of articles,
        // add the correct number of pages and the next button.
        if (this.articleQuotient > 0 && this.articleRemainder > 0) {

            for ( let i = 0; i < this.articleQuotient + 1; i++ ) {

                paginationHTML += '<li class="pagination__page">' + (i + 1) + '</li>'
            }

            paginationHTML += `
                <li id="pageNext" class="pagination__next">
                    <svg class="pagination__btn__svg" xmlns="http://www.w3.org/2000/svg" width="14px" height="14px" fill="currentColor" class="bi bi-chevron-right" viewBox="0 0 16 16">
                        <path fill-rule="evenodd" d="M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z"/>
                    </svg>
                </li>
            `

            document.getElementById('pagination').innerHTML = paginationHTML
        }
        // If there are more than 6 articles and there are no remainder of articles,
        // add the correct number of pages and the next button.
        else if (this.articleQuotient > 0 && this.articleRemainder === 0) {

            for ( let i = 0; i < this.articleQuotient; i++ ) {

                paginationHTML += '<li class="pagination__page">' + (i + 1) + '</li>'
            }

            paginationHTML += `
                <li id="pageNext" class="pagination__next">
                    <svg class="pagination__btn__svg" xmlns="http://www.w3.org/2000/svg" width="14px" height="14px" fill="currentColor" class="bi bi-chevron-right" viewBox="0 0 16 16">
                        <path fill-rule="evenodd" d="M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z"/>
                    </svg>
                </li>
            `

            document.getElementById('pagination').innerHTML = paginationHTML
        }
        // If there are less than 6 articles, but there are a remainder of articles,
        // only add one page and omit the next button.
        else if (this.articleQuotient === 0 && this.articleRemainder > 0) {

            paginationHTML = '<li class="pagination__page">1</li>'

            document.getElementById('pagination').innerHTML = paginationHTML
        }

        // Add event listeners to each page number
        // Call function to update list of articles
        let pageNumbers = Array.from( document.getElementsByClassName('pagination__page') )

        pageNumbers.forEach( (pageNumber) => {

            pageNumber.addEventListener('click', () => {

                // Store the page number clicked and get all articles on that page
                this.currentPageNumber = parseInt(pageNumber.innerHTML)
                this.pageNumberClick(this.currentPageNumber)
            })
        })

        // Add an event listener to the next button if it exists
        // Call function to update list of articles
        let pageNext = document.getElementById('pageNext')

        if (pageNext != null) {

            pageNext.addEventListener('click', () => {

                console.log('page next clicked!')
                this.pageNextClick(this.currentPageNumber)
            })
        }

    }

    static pageNumberClick(currentPageNumber) {
        /**
         * 
         */
        console.log('Running pageNumberClick()... Page:', currentPageNumber, 'Current topic:', this.currentTopicID, this.currentTopic)

        let APIFilterTopic = ''

        if (this.currentTopicID != undefined) {

            APIFilterTopic = `&topic=${this.currentTopicID}`
        }

        let APIOffset = `&offset=${ (6 * currentPageNumber) - 6 }`
        let url = `http://localhost:8000/api/v2/pages/?type=articles.ArticleDetailPage&fields=_,id,title,banner_text,topic,image,html_url,first_published_at&order=-first_published_at&limit=6`
        url += APIFilterTopic
        url += APIOffset

        this.fetchArticles(url)
    }

    static pageNextClick(currentPageNumber) {
        /**
         * 
         */
        console.log('pageNextClick()... ')
        console.log('this.articleQuotient=', this.articleQuotient)
        console.log('this.articleRemainder=', this.articleRemainder)
        console.log('pageNumber=', currentPageNumber)

        // If the current page number is less than or equal to the 
        if (currentPageNumber <= this.articleQuotient && this.articleRemainder > 0) {

            console.log('go to next page')
        }
        else {

            console.log('do not go to next page')
        }
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
         * Main method for loading articles. Adds event listeners
         * to each topic and will bring up the relevant articles.
         */
        let topicsAll = document.getElementById('topicsAll')
        let topics = Array.from( document.getElementsByClassName('topics__topic--topic') )

        // Highlight "All" topic on page load
        topicsAll.classList.add('clicked')

        // Set default pageNumber on load to 1
        this.currentPageNumber = 1

        // Get all articles on page load
        let url = 'http://localhost:8000/api/v2/pages/?type=articles.ArticleDetailPage&fields=_,id,title,banner_text,topic,image,html_url,first_published_at&order=-first_published_at&limit=6'
        this.fetchArticles(url)

        // When the user clicks "All", gets all the articles and displays them
        // Also applies background & color transition on topic click.
        topicsAll.addEventListener('click', () => {

            // Apply topic transitions
            this.topicTransitions(topicsAll)

            // Store the topic name and ID (used in pagination)
            this.currentTopic = 'All'
            this.currentTopicID = undefined

            // Get articles
            let url = 'http://localhost:8000/api/v2/pages/?type=articles.ArticleDetailPage&fields=_,id,title,banner_text,topic,image,html_url,first_published_at&order=-first_published_at&limit=6'
            this.fetchArticles(url)
        })

        // For each non-all topic clicked, fetch the respective articles.
        // Also applies background & color transition on topic click.
        topics.forEach( (topic) => {

            topic.addEventListener('click', () => {

                // Apply topic transitions
                this.topicTransitions(topic)

                // Store the topic name and ID (used in pagination)
                this.currentTopic = topic.dataset.topic_name
                this.currentTopicID = parseInt(topic.dataset.topic_id)

                // Adds a filter parameter to the API url
                let APIFilterTopic = `&topic=${topic.dataset.topic_id}`
                let url = `http://localhost:8000/api/v2/pages/?type=articles.ArticleDetailPage&fields=_,id,title,banner_text,topic,image,html_url,first_published_at&order=-first_published_at&limit=6`
                url += APIFilterTopic

                // Get articles
                this.fetchArticles(url)
            })
        })

    }

}

Articles.getArticles()