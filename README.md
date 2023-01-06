## Membuat Django Multivendor Restaurant 

Project ini dibuat berdasarkan kursus Rathan Kumar pada udemy.com
Github link: https://github.com/gurnitha/django-multivendor-restaurant
Udemy link: https://www.udemy.com/course/python-django-real-world-project-multi-vendor-restaurant/


## 00 Persiapan

#### 00.1 Modifikasi readme dan .gitignore file

        modified:   .gitignore
        modified:   README.md

#### 00.2 Mengisi TOC pada readme file

        modified:   README.md

#### 00.3 Modifikasi readme file

        modified:   README.md

## 01. Introduction

#### 1. Intro
		pass

#### 2. Full Project Overview/Demo
		pass

#### 3. Project Flowchart
		pass

#### 4. IMPORTANT!!! How To Get This Course For Lowest Price
		pass


## 02. Getting Ready


#### 5. Gitbash Vscode Installation
		pass

#### 6. Create Virtual Environment
		
		python -m venv venv3932
        modified:   README.md

#### 7. Install Django, Create Django Project and App

#### 7.1 Install Django

		λ .\venv3932\Scripts\activate.bat
		(venv3932) λ pip install django==3.2.*
		(venv3932) λ python.exe -m pip install --upgrade pip

        modified:   README.md
        new file:   manage.py
        
#### 8. Hello World

#### 9. GitHub Setup

#### 10. FoodOnline Full Project Git Repository

#### 11. Django Templates Setup

#### 12. Create Superuser



## 03. Template


#### 13. Purchase Foodbakery Template

#### 14. Template Walkthrough

#### 15. Homepage And Static Files Config

#### 16. Collectstatic



## 04. Database


#### 17. Why Postgres Intro

#### 18. Postgres Configuration With Django

#### 19. Store Sensitive Info And Push Code



## 05. Custom user model, Media files, dan Django signals


#### 20. Cutom User Model

#### 21. Recreate Table And Register User Model

#### 22. Make Password Noneditable

#### 23. Userprofile Overview

#### 24. User Profile Model

#### 25. Media Files Configuration

#### 26. Django Signals To Create User Profile



## 06. Custom User Model, Django Messages, Media Files and Django Signals


#### 27. Foodonline Flowchart

#### 28. User registration Path

#### 29. Template Inheritance Base Html

#### 30. User Registration Form Template

#### 31. User Registration Form Implementation

#### 32. Hash The Password From Form

#### 33. Django Field Errors And Non Field Errors

#### 34. Django Messages

#### 35. Messages Animation

#### 36. Frontend Tweaks

#### 37. Git Push



## 07. Vendor regisistration and authentication functionalities


#### 38. Vendor Model

#### 39. Vendor Registration Template

#### 40. Vendor Registration Feature

#### 41. Vendor Admin Config

#### 42. Login Page Setup

#### 43. Login Logout Feature

#### 44. Restrict Loggedin Users From Accessing Loginpage And Register Page

#### 45. Detect User And Redirect Him To Respective Dashboard

#### 46. Restrict The User To Access Unauthorized Pages

#### 47. Git Push


## 08. Token verification and email configuration


#### 48. Email Configuration

#### 49. Send Verification Email

#### 50. Activating The User

#### 51. Forgot Password Setup

#### 52. Forgot Password Send Validation Link

#### 53. Reset Password Feature

#### 54. Git Push


## 09. Vendor approval by admin and dashboard


#### 55. Admin Approval Email

#### 56. Setup Cust And Vendor Dashboard Frontend

#### 57. Dashboard Sidebar Icon Fix

#### 58. Vendor Dashboard Url Setup

#### 59. Load Vendor Profile Image Dynamically

#### 60. Get Vendor Context Processor

#### 61. Fix Anonymous User Error In Context Processors

#### 62. Make Dashboard Cards

#### 63. Git Push



## 10. Make restaurant profile form and custom validators


#### 64. Restaurant Profile Form Setup

#### 65. Store Vendor Profile

#### 66. Custom Validator Function Allow Only Images

#### 67. Readonly Latlong And Apply Decorator

#### 68. Prepare Address Field For Google Geocoding

#### 69. Git Push



## 11. Implement Google Autocomplete field


#### 70. Setup Google Maps Billing Account

#### 71. Enable Apis And Create Api Key

#### 72. Implement Google Autocomplete

#### 73. Get The Lat Long And Assign To Form Field

#### 74. Loop Through Address Components And Fetch Data

#### 75. Git Push



## 12. Menu Builder - Category CRUD functionalities


#### 76. Foodmenu Models Category And Fooditem Models

#### 77. Add Test Food And Setup Admin Table

#### 78. Menu Builder Url And View Setup

#### 79. Menu Builder Category Frontend Part1

#### 80. Menu Builder Fooditem Front End

#### 81. Add Category CRUD

#### 82. Add Category Handle Error

#### 83. Edit Category CRUD

#### 84. Delete Category CRUD

#### 85. Git Push



## 13. Menu Builder - Food Items CRUD functionalities


#### 86. Add Food Crud

#### 87. Edit Food Crud

#### 88. Delete Food Crud

#### 89. Url Path Adjustment And Availablity Badge

#### 90. Handle Empty Value Errors

#### 91. Mofidy The Form To Show Category Belongs To Loggedin Vendors

#### 92. Edit Food Category For Loggedin Vendors

#### 93. Git Push



## 14. Marketplcae implementation


#### 94. Show Vendors On Homepage

#### 95. Marketplace Button And Url Setup

#### 96. Marketplace Html And View

#### 97. Edit Vendor Model And Add Slug Field

#### 98. Vendor Detail Page Setup

#### 99. Dis Fooditems By Category Using Prefetch Related



## 15. Cart functionalities without refreshing the page - AJAX request


#### 100. Create Cart Model

#### 101. Add To Cart Url Setup

#### 102. Add To Cart Sending Ajax Request

#### 103. Add To Cart View Functionality Edited

#### 104. Cart Counter Context Processor

#### 105. Place The Quantiry On Each Food Item

#### 106. Update The Cart Counter And Item Qty Realtime

#### 107. Fix Google Maps Script Issue

#### 108. Decrease Cart Feature Edited

#### 109. Implement Sweetalert And Handle Messages



## 16. Cart functionalities with frontend


#### 110. Cart Url Setup

#### 111. Cart Page Content Setup

#### 112. Cart Items In The Cart

#### 113. Fix Cart Item Quantity

#### 114. Delete Cart Item

#### 115. Remove Cart Item Without Reloading The Page

#### 116. Check If Cart Is Empty

#### 117. Handle Decrease Cart Use Cases

#### 118. Show Vendor Name Badge And Add Order By Clause

#### 119. Get Cart Amounts Function To Get The Subtotal And Grand Total

#### 120. Update Subtotal Tax Grandtotal Without Refreshing The Page

#### 121. Git Push



## 17. Basic Search and Smart search functionalities


#### 122. Search Functionality Setup Search Bar

#### 123. Get Query Parameters From The Get Request

#### 124. Add Some Restaurants And Fooditems--Attach Checklist

#### 125. Basic Search For Restaurants

#### 126. Smart Search For Restaurants By Fooditem Name



## 18. Location based search functionalities with nearby restaurants


#### 127. Location based Search Requirements

#### 128. Geodjango Overview

#### 129. Install Postgis And Gdal

#### 130. Create Location Point And See Geometry Viewer

#### 131. Location Based Search For Restaurants

#### 132. Find The Nearby Restaurants

#### 133. Git Push



## 19. Get user's current location and show nearby restaurant on homepage


#### 134. Get Current Latitude Longitude

#### 135. Send Ajax Request To Get Current Address

#### 136. Show Nearby Restaurants On Homepage

#### 137. Set The Location In Session Variable

#### 138. Git Push



## 20. Dynamic Business hours module with AJAX&lt


#### 139. Opening Hours Overview

#### 140. Opening Hour Model

#### 141. Opening Hours Url And Sidebar

#### 142. Opening Hours Form

#### 143. Add Hour Url And Function

#### 144. Minor Adjustment To The Add Hour Form

#### 145. Send Ajax Request To Add Hour Function

#### 146. Add Hour To Database And Jsonresponse

#### 147. Handling Integrity Error

#### 148. Remove Opening Hour Feature

#### 149. Create Some Opening Hours-And Fix Unique Together Issue

#### 150. List Down Opening Hours In The Front End

#### 151. Determine Opeining Hour For Vendor Detail Page

#### 152. Is Open Member Function To Dis Open Close Badge

#### 153. Git Push



## 21. Dynamic Tax Module


#### 154. Dynamic Tax Module Create Model

#### 155. Calculate Tax Amount

#### 156. Implement Dynamic Tax In The Cart Page

#### 157. Update Tax In The Frontend

#### 158. Fixed Timedata Doesnot Match Issue

#### 159. Git Push



## 22. Customers app and profile building


#### 160. Create Customers App

#### 161. Customer Profile Path And Page

#### 162. Profile Form And User Form

#### 163. Prepopulate Forms

#### 164. Update Customer Profile

#### 165. Load Cover And Profile Pictures

#### 166. Git Push


## 23. Orders model and checkout page


#### 167. Order, Payment, and OrderedFood Models

#### 168. Checkout Page Setup

#### 169. Checkout Page Part 1

#### 170. Checkout Page Order Form Part 2

#### 171. List Cart Items In Checkout Page

#### 172. Prepopulate Billing Form



## 24. Place order and generate order number


#### 173. Payment Gateway Selection On Checkout Page

#### 174. Payment Method Selection Validation

#### 175. Make Place Order Path And Page

#### 176. Place Order View

#### 177. Generate Order Number



## 25. Implement PayPal payment gateway


#### 178. Create Paypal Business Account

#### 179. Create Paypal Sandbox Accounts

#### 180. Paypal Checkout Button Implementation

#### 181. Send Transaction Function

#### 182. Update Place Order Page With Review Order And Cart Items

#### 183. Store Payment Object And Update Order



## 26. After order functionalities


#### 184. Move Cart Items To Ordered Food And Create Tabular Inline

#### 185. Send Order Confirmation Email To Customer

#### 186. Send Order Received Email To Vendor And Clear Cart

#### 187. Order Completion Page Setup

#### 188. Order Complete View

#### 189. Implement Order Completion Page-Part1

#### 190. Implement Order Completion Page Part2

#### 191. Print Address On Order Complete Page

#### 192. Git Push


## 27. Implement RazorPay Payment Gateway


#### 193. Show Payment Button Based On Payment Method Selected

#### 194. Razorpay Basic Configuration

#### 195. Create Rzp Order

#### 196. Razorpay Checkout

#### 197. Finalize Razorpay Payments

#### 198. Git Push



## 28. Customer Dashboard


#### 199. Customer Dashbord Recent Orders

#### 200. Customer My Orders

#### 201. Order Detail Setup

#### 202. Order Detail Page Finish

#### 203. Git Push



## 29. ManyToMany Relationship and Vendor Dashboard


#### 204. Many To Many Relationship Overview

#### 205. Many To Many Create Field And Test Orders

#### 206. Total Orders Vendor Dashboard

#### 207. Recent Orders Vendor Dashboard

#### 208. Assign Vendors To Order

#### 209. Order Detail Page Vendor

#### 210. Calculate Subtotal For Each Vendor


## 30. Custom middleware, total revenue per vendor, current month's revenue


#### 211. Create Custom Middleware And Get Total By Vendor Function

#### 212. Calculate Vendor Order Total Data

#### 213. Update Total In Order Detail Page

#### 214. Calculate Total Revenue Per Vendor

#### 215. Calculate Current Month Revenue

#### 216. Vendor My Orders

#### 217. Implement Datatable Plugin For Pagination And Realtime Order Search

#### 218. Payout System Announcement

#### 219. Git Push



## 31. Integrate Email Templates


#### 220. Register User Account Email Template

#### 221. Order Confirmation Email To Customer Template Part 1

#### 222. Order Confirmation Email To Customer Template Part 2

#### 223. Order Received Email Template To Vendor

#### 224. Git Push



## 32. Make the site mobile-friendly (responsive)


#### 225. Responsiveness-Part-1

#### 226. Responsiveness-Part-2



## 33. Project Deployment on Linode Virtual Private Server


#### 227. Linode Overview

#### 228. Server Overview

#### 229. How Nginx And Gunicorn Works Together

#### 230. Deployment Checklist

#### 231. Signup to Linode & Create Server

#### 232. Create Domain Nameservers

#### 233. Basic Server Setup - Create a Sudo User

#### 234. Possible deployment issues & Get the local code ready to be pushed to server

#### 235. Setup GIT to push code from local server to live server

#### 236. Install & Configure PostgreSQL on Live Server

#### 237. Setup Virtual Environment on Live Server

#### 238. Install GDAL and PostGIS on Live Server

#### 239. Dumpdata and Loaddata on Live Server

#### 240. Gunicorn Configuration

#### 241. Nginx Configuration

#### 242. Fix Static Files on Server

#### 243. Install SSL on Live Site

#### 244. Uncomment user's current location code for live website

#### 245. Congratulations! You made it!
