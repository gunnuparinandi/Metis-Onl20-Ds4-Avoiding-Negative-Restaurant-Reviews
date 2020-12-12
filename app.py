import streamlit as st

# NLP pksgs
import json
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

data = pd.read_csv('/Users/gunnuparinandi/Desktop/unsampled_weights.csv')
data = data.drop('Unnamed: 0', 1)



def main ():
	"""NLP App with Steamlit"""

	st.title("Restaurant Token Analyzer")
	st.subheader("If token weight < 0 - work on these things. If token weight > 0 -  keep up the good work!")


	#Tokenization

	message = st.text_area("Enter the word of your choice: Type Here")
	if st.button("Analyze"):

		st.dataframe(data[data.token==message].log_reg_coefficient)
		#st.success(message.title())



if __name__ == '__main__':
	main()