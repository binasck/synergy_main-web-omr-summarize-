from summarizer import Summarizer, TransformerSummarizer
body="Privatization is the process by which the government transfers ownership and control of economic units to the private sector. " \
     "The primary tenet of privatisation is that the competitive environment and market system compel corporations and private entities to function more efficiently." \
     " Littlechild and Beesley (1989) believe that privatisation can improve economic performance by increasing market forces, provided that at least 50% of their shares are transferred to the private sector. " \
     "Privatization is a broad and diverse phrase that refers to the process by which the private sector assumes operational or financial control of public institutions. In other words, privatisation entails the abolition of all government controls and involvement in the establishment of supply and demand mechanisms. " \
     "Banks are significant because they play a critical role in the economy. " \
     "According to Levine (1997), a critical variable in the process of financial development and economic growth is the ownership structure of banks and their fundamental role in the national economy. " \
     "The banking sector’s primary objective is to move financial resources into more productive and efficient initiatives that will aid future growth. " \
     "The government’s job in the financial system is to ensure that banks perform this critical function efficiently through their rules and regulations. " \
     "As a result of this critical role, governments in developing nations frequently hold banks. " \
     "The profit incentive is said to motivate the private sector to manage a business more efficiently. " \
     "However, private corporations can exploit their dominant strength while ignoring greater social costs, say opponents. " \
     "The first and most essential cause for privatisation is the weakening economy. " \
     "The ongoing pandemic has significantly harmed the Indian economy, prompting the government to take such drastic disinvestment measures." \
     " The growing NPA issue has further fueled the privatisation drive. " \
     "Because of their welfare state programmes and loan forgiveness, PSBs contribute the most to NPA. The government wants to reduce the NPA problem and relieve the PSBs by privatising them. " \
     "Dual control is also an issue, with the Ministry of Finance having dual jurisdiction over PSBs under the Banking Regulation Act, 1949, and the Reserve Bank Act, 1934. " \
     "Instead of being autonomous like private banks, the RBI is constantly interfering with routine PSB operations. " \
     "With an economic and political analysis of the decision, the privatisation of PSBs has sparked a large national debate.  " \
     "Privatisation has both beneficial and negative effects on the Indian economy."
bert_model = Summarizer()
bert_summary = ''.join(bert_model(body, min_length=60))
print(bert_summary)