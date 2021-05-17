from pyppeteer import launch


async def get_page(url):
    browser = await launch({'args': ['--window-size=1920,1080'], 'defaultViewport': None})
    page = await browser.newPage()
    await page.goto(url)
    total_height = await page.evaluate('''() => {
        return document.body.parentNode.scrollHeight
    }''')
    total_width = await page.evaluate('''() => {
        return document.body.offsetWidth
    }''')
    await page.setViewport({'width': total_width, 'height': total_height})
    await page.waitFor(500)

    img = await page.screenshot()
    await browser.close()
    return img
