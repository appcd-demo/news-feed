import feedparser

def lambda_handler(event, context):
    
    feed_url = 'https://lwkd.info/feed.xml'
    
    
    feed = feedparser.parse(feed_url)
    
    
    html_content = "<html><body>"
    html_content += f"<h1>{feed.feed.title}</h1>"
    
    for entry in feed.entries:
        html_content += f"<h2><a href='{entry.link}'>{entry.title}</a></h2>"
        html_content += f"<p><em>Published: {entry.published}</em></p>"
        html_content += f"<p>{entry.summary}</p>"
        html_content += entry.get('content', [{'value': entry.summary}])[0]['value']
        html_content += "<hr>"
    
    html_content += "</body></html>"
    
    # Return the feed items as HTML
    return {
        'statusCode': 200,
        'body': html_content,
        'headers': {
            'Content-Type': 'text/html'
        }
    }
