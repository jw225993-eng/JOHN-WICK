# 🃏 Blackjack Pro Advisor

A Streamlit-based Blackjack strategy advisor that provides optimal gameplay recommendations based on your current hand and the dealer's visible card.

## Features

- **Real-time Strategy Advice**: Get instant recommendations on whether to Hit or Stand
- **Soft Hand Detection**: Handles Ace-based soft hands correctly
- **Bilingual Interface**: English and Bengali support
- **Interactive UI**: Easy-to-use input controls with visual feedback

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jw225993-eng/JOHN-WICK.git
cd JOHN-WICK
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the App

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## Deployment

### Streamlit Cloud (Recommended)

1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app"
4. Select your repository and branch
5. Set the main file to `app.py`
6. Click "Deploy"

### Other Deployment Options

- **Heroku**: Use the Procfile configuration
- **Docker**: Create a Docker image with Python and Streamlit
- **AWS/Azure**: Deploy using their respective container services

## Usage

1. Enter your current Blackjack score (2-21)
2. Check if you have a soft Ace (11)
3. Enter the dealer's visible card (2-11)
4. Click "পরামর্শ নিন" (Get Advice) to receive a recommendation

## Strategy

The advisor uses basic Blackjack strategy:
- **Soft hands (with Ace as 11)**: Stand on 19+, specific rules for 18 and below
- **Hard hands**: Stand on 17+, conditional rules based on dealer card
- Optimal play against dealer's up card

## License

This project is open source and available under the MIT License.
