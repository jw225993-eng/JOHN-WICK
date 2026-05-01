import streamlit as st

# বটের মূল লজিক ফাংশন
def get_advice(player_total, dealer_card, is_soft):
    if is_soft:
        if player_total >= 19: return "Stand (থামুন)"
        elif player_total == 18:
            return "Stand (থামুন)" if dealer_card in [2, 7, 8] else "Hit (কার্ড নিন)"
        else: return "Hit (কার্ড নিন)"
    
    if player_total >= 17: return "Stand (থামুন)"
    elif 13 <= player_total <= 16:
        return "Stand (থামুন)" if dealer_card <= 6 else "Hit (কার্ড নিন)"
    elif player_total == 12:
        return "Stand (থামুন)" if dealer_card in [4, 5, 6] else "Hit (কার্ড নিন)"
    else: return "Hit (কার্ড নিন)"

# ওয়েবসাইটের ডিজাইন অংশ
st.set_page_config(page_title="Blackjack Bot", page_icon="🃏")
st.title("🃏 Blackjack Pro Advisor")
st.markdown("আপনার গেমের বর্তমান অবস্থা নিচে ইনপুট দিন:")

# ইনপুট নেওয়ার জন্য কলাম তৈরি
col1, col2 = st.columns(2)

with col1:
    player_score = st.number_input("আপনার বর্তমান স্কোর", min_value=2, max_value=21, value=14)
    is_soft = st.checkbox("আপনার হাতে কি Ace (১১ হিসেবে ধরা) আছে?")

with col2:
    dealer_card = st.number_input("ডিলারের সামনের কার্ড (Ace=11)", min_value=2, max_value=11, value=10)

# বাটন এবং আউটপুট
if st.button("পরামর্শ নিন"):
    advice = get_advice(player_score, dealer_card, is_soft)
    if "Hit" in advice:
        st.error(f"বটের পরামর্শ: **{advice}**")
    else:
        st.success(f"বটের পরামর্শ: **{advice}**")
