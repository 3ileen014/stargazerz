import stargazerz

crawler = stargazerz.Crawler(threads=10, target="bricks-cloud/BricksLLM")

crawler.run()
crawler.print_results()
crawler.save_results("emails", "emails.txt")
crawler.save_results("stargazers", "stargazers.txt")
crawler.save_results("all", "all.txt")