import streamlit as st
import requests
from streamlit_lottie import st_lottie
import streamlit as st
from PIL import Image
import base64
import io


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout='wide')


hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem; padding-left:0rem; padding-right:0rem;}
</style>
"""

# Memastikan CSS diterapkan langsung saat aplikasi dijalankan
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# Fungsi untuk mengonversi gambar ke format Base64
def convert_image_to_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

# Memuat gambar dengan PIL
image = Image.open('images/AI.jpeg')
image_base64 = convert_image_to_base64(image)
image_base60 = convert_image_to_base64(image)

# Menyisipkan link Bootstrap 5 ke dalam aplikasi Streamlit
st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
""", unsafe_allow_html=True)

# Membaca file CSS dari file terpisah
with open("style/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


# Banner

# Membaca gambar dan mengonversinya ke Base64
with open("images/AI.jpeg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

# Menyisipkan gambar Base64 ke dalam tag <img>
st.markdown(f"""
<div class="container-fluid banner">
    <div class="container banner-content">
        <div class="row">
            <div class="col-md-6 gambar1">
                <div class="gambar mt-3">
                    <img src="data:image/jpeg;base64,{encoded_string}" alt="AI Image">
                </div>
            </div>
            <div class="col-md-6 text1">
                <h1 class="judul1 text-center text-lg-start">Waste</h1>
                <p class="paragraft1 mb-4">Artificial intelligence (AI), in its broadest sense, is 
                    intelligence exhibited by machines, particularly computer 
                    systems. It is a field of research in computer science that 
                    develops and studies methods and software that enable machines 
                    to perceive their environment and use learning and intelligence 
                    to take actions that maximize their chances of achieving defined 
                    goals.[1] Such machines may be called AIs.
                </p>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)



# st.write("##")
with st.container():
    st.write("---")



# About
st.markdown("<h1 style='text-align: center;'>About</h1>", unsafe_allow_html=True)
st.markdown("""
    <div class="container-fluid">
        <div class="container">
            <p class="text-center mb-4">AI sudah mulai diterapkan di berbagai sektor di Indonesia, 
                mulai dari logistik, Sumber Daya Manusia (SDM), 
                pendidikan, keamanan siber, hingga layanan pelanggan. 
                Penerapan AI meningkatkan efisiensi operasional dan 
                memungkinkan bisnis untuk menyediakan produk AI 
                yang meningkatkan produktivitas klien. Berikut adalah 
                beberapa contoh penerapan teknologi AI yang diterapkan 
                saat ini, termasuk yang ada di dalam ekosistem East Ventures.
            <p>
            <div class="text-center mb-4">
                <a href="/about" target="_self"><button class="btn btn-success">Baca Selengkapnya</button></a>
            </div>
        </div>
    </div>    
""", unsafe_allow_html=True)

with st.container():
    st.write("---")




# Menyusun Card dan HTML dengan gambar Base64
st.markdown(f"""
    <div class="container-fluid">
        <div class="container">
            <h2 class="text-center">Project</h2>
            <div class="row">
                <div class="col-lg-3 col-md-6 mb-4 col-sm-6">
                    <div class="card bg-dark text-white">
                        <img src="data:image/jpeg;base64,{image_base64}" class="card-img-top" alt="Deskripsi gambar AI">
                        <div class="card-body">
                            <h5 class="card-title">AI</h5>
                            <p class="card-text">jfjhjahf jfjh jkas jkjkaf jk h</p>
                            <button class="btn btn-primary">Lihat</button>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6 mb-4 col-sm-6">
                    <div class="card bg-dark text-white">
                        <img src="data:image/jpeg;base64,{image_base64}" class="card-img-top" alt="Deskripsi gambar AI">
                        <div class="card-body">
                            <h5 class="card-title">AI</h5>
                            <p class="card-text">jfjhjahf jfjh jkas jkjkaf jk h</p>
                            <button class="btn btn-primary">Lihat</button>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6 col-sm-6 mb-4">
                    <div class="card bg-dark text-white">
                        <img src="data:image/jpeg;base64,{image_base64}" class="card-img-top" alt="Deskripsi gambar AI">
                        <div class="card-body">
                            <h5 class="card-title">AI</h5>
                            <p class="card-text">jfjhjahf jfjh jkas jkjkaf jk h</p>
                            <button class="btn btn-primary">Lihat</button>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6 mb-4 col-sm-6">
                    <div class="card bg-dark text-white">
                        <img src="data:image/jpeg;base64,{image_base64}" class="card-img-top" alt="Deskripsi gambar AI">
                        <div class="card-body">
                            <h5 class="card-title">AI</h5>
                            <p class="card-text">jfjhjahf jfjh jkas jkjkaf jk h</p>
                            <button class="btn btn-primary">Lihat</button>
                        </div>
                    </div>
                </div>
            </div>
        </div> 
    </div> 
""", unsafe_allow_html=True)


with st.container():
    st.write("---")



# saran dan masukan
st.markdown("""
    <h1 class="text-center">
        Saran dan Mauskan
    </h1>
""",unsafe_allow_html=True)

st.markdown("""
    <div class="container-fluid">
        <div class='container message'>
            <div class="row">
                <div class="col-6">
                    <form action="https://formsubmit.co/kevinsepoetro@gmail.com" method="POST">
                        <input type="hidden" name="_captcha" value="false">
                        <div class="mb-3">            
                            <label class="form-label">Name</label>
                            <input type="text" name="name" placeholder="Your Name" required class="form-control">
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Email</label>
                            <input type="email" name="email" placeholder="Email" required class="form-control">
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Masukan</label>
                            <textarea name="message" placeholder="Your message here" required class="form-control"></textarea>
                        </div>
                        <button class="btn btn-primary" type="submit">Send</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
""",unsafe_allow_html=True)




# Kontak
print()