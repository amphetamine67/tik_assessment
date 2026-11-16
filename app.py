from flask import Flask, abort, render_template

app = Flask(__name__)

info_toko = {
    "nama_toko": "GGmaxxing Shop",
    "slogan": "Play It with Your Own Way",
    "lokasi": "Lampung, Indonesia",
    "wa_link": "https://wa.me/inputnum?text=Halo%2C%20saya%20mau%20beli%20barang%20ini.",
}

daftar_produk = [
    # Mouse
    {
        "nama_produk": "Logitech G PRO X SUPERLIGHT 2 | LIGHTSPEED Wireless Gaming Mouse",
        "harga": 2500000,
        "id_produk": "ms0001"
    },

    {
            "nama_produk": "Pulsar Pro Series Jinggg-X Gaming Mouse | Pink",
            "harga": 2357000,
            "id_produk": "ms0002"
    },

    # Keyboard
    {
        "nama_produk": "Wooting 60HE+ | Compact Gaming Keyboard",
        "harga": 2850000,
        "id_produk": "kb0001"
    },

    {
            "nama_produk": "ASUS ROG Falcata | Wireless Mechanical Gaming Keyboard",
            "harga": 5000000,
            "id_produk": "kb0002"
        },

    # Switch
    {
        "nama_produk": "OWLAB Ti Hall-Effect Linear Magnetic Switches",
        "harga": 107000,
        "id_produk": "swt0001"
    },

    # Monitor
    {
        "nama_produk": "BenQ ZOWIE XL2540X+ 24.1 | New Fast TN 280Hz Gaming Monitor 1080p",
        "harga": 6666000,
        "id_produk": "mo0001"
    },

    # Mouse Pad
    {
        "nama_produk": "Razer Atlas | Tempered Glass Gaming Mouse Mat",
        "harga": 1990000,
        "id_produk": "mspd0001"
    },

    # Graphics Card
    {
        "nama_produk": "MSI GeForce RTX™ 5070 Ti 16G MLG EDITION",
        "harga": 27298000,
        "id_produk": "gc0001"
    },

    # Headset
    {
            "nama_produk": "HyperX Cloud III | Gaming Headset",
            "harga": 3021000,
            "id_produk": "hs0001"
    },

    # In Ear Monitor
    {
            "nama_produk": "ORIVETI bleqk Dynabird | Single Dynamic Driver HiFi IEM",
            "harga": 1795000,
            "id_produk": "iem0001"
    },

    # CPU Cooler
    {
            "nama_produk": "CoolerMaster MasterLiqiud Atmos II Stealth 240",
            "harga": 2107500,
            "id_produk": "ac0001"
    }
    ]
@app.route('/')
def home():
    return render_template('index.html', data=info_toko, produk=daftar_produk)


@app.route('/produk/<id_produk>')
def product_detail(id_produk):
    produk = next(
        (produk for produk in daftar_produk if produk["id_produk"] == id_produk),
        None,
    )
    if produk is None:
        abort(404)

    data = {**info_toko, **produk}
    return render_template('detail.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)