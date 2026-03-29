#Oil Reserve Calculator

This is a web application that helps us figure out how much oil we can get from a reservoir. It uses a formula that petroleum engineers use. I built this as a project for my CSA2001. Fundamentals of AI and ML course at VIT Bhopal.

---

#What This Project Does

When people think they have found an oil reservoir they need to know how much oil is really there before they start drilling. This calculator takes a basic things about the reservoir and gives us an idea of how much oil is there and how much we can actually get out.

It is not a tool that companies would use every day. It uses the same formula that they use. I wanted to understand how the geological parameters affect the amount of oil we can get and how to connect that to a web application.

---

#Files

- `app.py`. This is the backend, written in Python using Flask. It takes the input values does the calculation and sends back the result.

- `index.html`. This is the frontend. It is a HTML page where you enter the values and see the output.

---

#Formula Used

Oil Reserve Calculator uses a formula called STOIIP, which stands for Stock Tank Oil Initially In Place. The formula is:

```

STOIIP = 7758 x Area x Thickness x Porosity x (1. Water Saturation) / Bo

```

Where:

- 7758 is a number that helps us convert units

- Area's the size of the reservoir in acres

- Thickness is how thick the oil layer is in feet

- Porosity is how much of the rock is empty space where the oil can sit

- Water Saturation is how much of that empty space is already filled with water

- Bo is a number that accounts for the oil shrinking when it comes to the surface

Then we estimate how much oil we can actually get by multiplying the Oil Reserve Calculator result by a recovery factor, which depends on how good the reservoir is.

---

#How to Run

First you need to have Python installed. Then you need to install two things:

```

pip install flask flask-cors

```

Next you run the backend:

```

python app.py

```

This will start a server at http://localhost:5000. Keep this window open.

Then you can open `index.html` in your browser by clicking it.

Enter some values in the form. Click Calculate. The result will show up below.

---

#Input Parameters

| Parameter | Unit | Example |

|---|---|---|

| Reservoir Area | acres | 500 |

Net Thickness | feet | 100 |

Porosity | percent | 18 |

| Water Saturation | percent | 30 |

---

#Limitations

The recovery factor in this version is a rough guess based only on porosity. In life it depends on many things like how the oil flows how thick the oil is and the pressure in the reservoir. I kept it simple, for this project.

---

#Dependencies

- Python 3.x

- Flask

- Flask-CORS

---

#References

- Craft, B.C. And Hawkins, M.. Applied Petroleum Reservoir Engineering

- volumetric method. SPE Petroleum Engineering Handbook

- Course material: CSA2001, VIT Bhopal
