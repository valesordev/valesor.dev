import unittest
from unittest.mock import patch, Mock, mock_open
import json
from datetime import datetime
from bs4 import BeautifulSoup
from scrape import APNewsScraper


class TestAPNewsScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = APNewsScraper()

        # Load test data
        with open("https_apnews_com.html", "r", encoding="utf-8") as file:
            self.sample_homepage = file.read()

        with open("https_apnews_com-article.html", "r", encoding="utf-8") as file:
            self.sample_article = file.read()

        # Expected test data
        self.expected_article = {
            "url": "https://apnews.com/article/palestinians-unrwa-israel-netanyahu-hamas-refugees-conflict-jerusalem-13e94715d88b094834bd93c48d018bec",
            "headline": "",
            "content": "In the Shuafat refugee camp, a hardscrabble district in east Jerusalem surrounded by a hulking concrete wall, intense security checks make venturing out exasperating. In the absence of municipal services, the United Nations agency for Palestinian refugees, known as UNRWA, is what provides decent free healthcare and education to Shuafat’s residents. Those services — as well as everything from garbage pickup to maintaining water systems — may begin disappearing after Thursday, when a pair of Israeli laws passed last October come into effect, banning UNRWA from operating on Israeli territory and prohibiting Israeli officials from having any contact with the agency. (AP video/Sam McNeil and Alon Bernstein) Palestinians gather outside of a health clinic run by the United Nations agency for Palestinian refugees, known as UNRWA, in the Shuafat refugee camp in Jerusalem, Monday, Jan. 27, 2025. (AP Photo/Mahmoud Illean) Women wait to be served at a health clinic run by the United Nations agency for Palestinian refugees, known as UNRWA, in the Old City of Jerusalem, Tuesday, Jan. 28, 2025. (AP Photo/Mahmoud Illean) Jonathan Fowler, senior communications manager for the United Nations agency for Palestinian refugees, known as UNRWA, pauses at a compound in the Shuafat refugee camp in Jerusalem, Monday, Jan. 27, 2025. (AP Photo/Mahmoud Illean) Two youths leave a boys school run by the United Nations agency for Palestinian refugees, known as UNRWA, in the Shuafat refugee camp in Jerusalem, Monday, Jan. 27, 2025. (AP Photo/Mahmoud Illean) Palestinians are seen in the Shuafat refugee camp in Jerusalem, Monday, Jan. 27, 2025. (AP Photo/Mahmoud Illean) A health clinic run by the United Nations agency for Palestinian refugees, known as UNRWA, is seen in the Old City of Jerusalem, Tuesday, Jan. 28, 2025. (AP Photo/Mahmoud Illean) The Shuafat refugee camp is seen in Jerusalem, Monday, Jan. 27, 2025. (AP Photo/Mahmoud Illean)                JERUSALEM (AP) — In the Shuafat refugee camp, a hardscrabble district in east Jerusalem surrounded by a concrete wall, cars inched their way toward an Israeli checkpoint. Intense security makes venturing out of the camp exasperating. But 42-year-old Areej Taha didn’t need to leave for medical treatment Monday. She had her toothache treated and picked up her insulin shots at a U.N.-run neighborhood clinic a block from where her kids were finishing their day at a U.N.-run school. In the absence of municipal services, the United Nations agency for Palestinian refugees, known as UNRWA, is the main provider of decent free healthcare and education to residents of Shuafat camp. If UNRWA left, Taha said, “I don’t want to have to think about what we would do.” But those services and everything from garbage pickup to water-system maintenance may begin disappearing after a pair of Israeli laws come into effect Thursday banning UNRWA from operating on Israeli territory and prohibiting Israeli officials from any contact with the agency. The most immediate impact will be in east Jerusalem, which Israel seized during the 1967 Mideast war and annexed in a move not recognized by most of the world. UNRWA’s headquarters there faces immediate shutdown. The bans passed by the Israeli legislature in October also threaten UNRWA’s operations across the occupied West Bank and Gaza Strip, where it is the lifeline for some 2 million Palestinians, most of whom are homeless from the 15-month Israel-Hamas war. Israel has long criticized UNRWA, contending it perpetuates Palestinians’ refugee status. The campaign against the agency has intensified from Prime Minister Benjamin Netanyahu and other right-wing politicians since Hamas’ Oct. 7, 2023 attack on southern Israel. Israeli claims that around a dozen of UNRWA’s 13,000 employees in Gaza participated in the attack and that many others support or sympathize with Hamas. The agency denies knowingly aiding armed groups and says it acts quickly to purge any suspected militants among its staff. How the legislation will be implemented and whether UNRWA operations will have to halt was unclear Wednesday, hours before the laws go into effect. Even UNRWA officials said they didn’t know what will happen. Israeli government spokesman David Mencer flatly said Wednesday that UNRWA will be banned from operating in Israel “in 48 hours.” Leeron Iflah, deputy director-general of Israel’s Jerusalem Affairs Office, told The Associated Press that “starting next week, all the kids in UNRWA schools will get placed in all kinds of schools in east Jerusalem.” But an Israeli government official with knowledge of the law’s details said there was no intention to physically shut institutions, only that it will become harder for the agency to operate without coordinating with Israeli authorities. The official spoke on condition of anonymity to discuss the plans. A total shutdown would end primary healthcare for up to 80,000 Palestinians in east Jerusalem through some two dozen medical centers, UNRWA officials say. It would also halt education and vocational training for up to 1,000 kids in the middle of a school year. “Now he’s supposed to leave school? Go where? How? He just started liking school,” said municipal worker Karim Hawash, looking over at his 13-year-old son who was kicking a soccer ball against the wall in Shuafat camp. “Already the schools here are so overcrowded.” There are no municipal schools inside the camp, meaning kids who leave UNRWA schools would have to make their way in and out daily through the Israeli checkpoints to still-unknown destinations. The immediate effect on UNRWA’s work in the West Bank or Gaza Strip is unknown but aid workers say the crackdown threatens UNRWA’s role as the backbone of humanitarian logistics in the region. Shutting down the headquarters “will impact everything that we are able to do,” Jonathan Fowler, UNRWA’s senior communications manager, said from the east Jerusalem compound. The agency provides a vast sweep of basic services to 1.1 million Palestinians in the West Bank and 2 million in Gaza. During the Israel-Hamas war, it has been the main agency ensuring delivery of food, medical supplies and other aid that Gaza’s population relies on to survive. UNRWA uses storage facilities in Israel for Gaza-bound aid convoys and needs to communicate with Israeli authorities who control access to Gaza to move material in and out — now threatened by the crackdown. Mencer said “aid needs to be redirected” to other U.N. agencies and other NGOs operating in Gaza. In the West Bank as well, UNRWA employees “won’t have freedom of movement like they did before,” said Arieh King, a deputy mayor of Jerusalem. “They cannot get in and out of Israel through the borders, the checkpoints.” Born from one of the most sensitive issues in the Israeli-Palestinian conflict, the fate of Palestinian refugees, UNRWA is no stranger to controversy. When roughly 700,000 Palestinians fled or were forced from their homes during the 1948 war over Israel’s creation, an event Arabs call the Nakba, or “catastrophe,” Israel refused to let them return. Arab governments resisted their integration. In 1949, the U.N. General Assembly created UNRWA to help this population sleeping in the open and clutching their house keys. It was meant to be temporary, until a political end to the Israeli-Palestinian conflict could be reached. But the system became permanent. The roughly 1 million Palestinians who landed on UNRWA’s rolls after fleeing the wars in 1948 and 1967 have become almost 6 million, in the West Bank, Gaza, Jordan, Lebanon and Syria. The dozens of tent camps that UNRWA set up decades ago across the Middle East have been built up into dense neighborhoods of apartment blocks and humming markets. “The international community has decided over and over that we should continue doing what we do because there has not been a just and lasting solution,” Fowler said. “There are not the sort of functioning state structures that can provide these kinds of services.” Israel has long argued that the agency perpetuates the conflict by maintaining a steadily growing refugee population. President Donald Trump has also been hostile to the agency, cutting off funding during his first term. UNRWA’s defenders believe Israel’s efforts to eliminate the agency have to do with wanting Palestinian refugees to give up hopes of returning to old homes in what is now Israel. Home to 7 million Jews, Israel says a large-scale return of Palestinian refugees would end its Jewish majority. In Shuafat refugee camp, Palestinians whose families fled there in 1948 have the coveted blue IDs of Jerusalem residents, allowing them to travel anywhere Israeli citizens may go. They pay taxes to the Israeli municipality and are subject to Israeli law. But in 2002, when Israel erected its separation barrier with the stated purpose of keeping out suicide bombers, Shuafat camp was left outside the wall, severed from the rest of the city by checkpoints and stranded in a political and bureaucratic limbo. The camp’s population exploded as Palestinians from the West Bank, although not allowed to live there, realized that no one was enforcing the rules. Israeli officials insist they’re committed to improving services for Palestinians in east Jerusalem but say it’s a long road. “It can’t work in one day,” Iflah said when asked how the municipality planned to replace UNRWA in Shuafat camp. In just a few days, though, Taha will need more insulin. With no blue ID — meaning she can’t enter Jerusalem — she doesn’t know what she’ll do.  ",
            "timestamp": "2025-01-29T13:07:23.552088",
        }

    @patch("requests.Session")
    def test_get_articles_homepage_parsing(self, mock_session):
        # Mock the session responses
        mock_response = Mock()
        mock_response.text = self.sample_homepage
        mock_session.return_value.get.return_value = mock_response

        # Count article links
        soup = BeautifulSoup(self.sample_homepage, "html.parser")
        article_links = [
            link
            for link in soup.find_all("a", href=True)
        ]

        self.assertEqual(
            len(article_links),
            787,
            "Should find exactly 787 article links in sample homepage",
        )

    @patch("requests.Session")
    @patch("time.sleep")  # Mock sleep to speed up tests
    def test_process_single_article(self, mock_sleep, mock_session):
        # Mock the session response
        mock_response = Mock()
        mock_response.text = self.sample_article
        mock_session.return_value.get.return_value = mock_response

        # Mock datetime to get consistent timestamps
        with patch("datetime.datetime") as mock_datetime:
            mock_datetime.now.return_value = datetime(2025, 1, 29)

            article_data = self.scraper._process_article(
                "https://apnews.com/article/test-article-1"
            )

            # Test URL
            self.assertEqual(article_data["url"], self.expected_article["url"])

            # Test headline
            self.assertEqual(
                article_data["headline"], self.expected_article["headline"]
            )

            # Test content
            self.assertEqual(article_data["content"], self.expected_article["content"])

            # Test timestamp
            self.assertEqual(
                article_data["timestamp"], self.expected_article["timestamp"]
            )

    @patch("requests.Session")
    @patch("time.sleep")  # Mock sleep to speed up tests
    def test_get_articles_with_limit(self, mock_sleep, mock_session):
        # Mock responses for homepage and articles
        mock_responses = {
            "https://apnews.com": Mock(text=self.sample_homepage),
            "https://apnews.com/article/test-article-1": Mock(text=self.sample_article),
            "https://apnews.com/article/test-article-2": Mock(text=self.sample_article),
            "https://apnews.com/article/test-article-3": Mock(text=self.sample_article),
        }

        def mock_get(url, *args, **kwargs):
            return mock_responses[url]

        mock_session.return_value.get.side_effect = mock_get

        # Test with limit of 2 articles
        articles = self.scraper.get_articles(max_articles=2)
        self.assertEqual(len(articles), 2, "Should respect max_articles limit")

    def test_save_articles(self):
        test_articles = [self.expected_article]
        mock_file = mock_open()

        with patch("builtins.open", mock_file):
            filename = self.scraper.save_articles(test_articles, "test_output.json")

            # Verify file operations
            mock_file.assert_called_once_with("test_output.json", "w", encoding="utf-8")

            # Verify written content
            handle = mock_file()
            written_data = json.loads(
                "".join(call.args[0] for call in handle.write.call_args_list)
            )
            self.assertEqual(written_data, test_articles)

    @patch("requests.Session")
    @patch("time.sleep")  # Mock sleep to speed up tests
    def test_error_handling(self, mock_sleep, mock_session):
        # Test network error
        def raise_network_error(*args, **kwargs):
            raise Exception("Network error")
        mock_session.return_value.get.side_effect = raise_network_error
        articles = self.scraper.get_articles(max_articles=1)
        self.assertEqual(len(articles), 0, "Should handle network errors gracefully")

        # Test malformed HTML
        mock_response = Mock()
        mock_response.text = "<malformed>>html>"
        mock_session.return_value.get.return_value = mock_response
        article_data = self.scraper._process_article(
            "https://apnews.com/article/test-article-1"
        )
        self.assertIsNone(article_data, "Should handle malformed HTML gracefully")


if __name__ == "__main__":
    unittest.main()
