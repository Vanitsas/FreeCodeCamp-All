# Design a Piano

This project is part of the FreeCodeCamp Responsive Web Design Certification.

## 📌 Project Overview

In this lab, a visual piano layout is built using HTML and CSS. The goal is to practice layout structure, positioning, pseudo-elements, and responsive design techniques.

The piano consists of white and black keys styled entirely with CSS. Black keys are generated using the .black--key::after pseudo-element to simulate a realistic piano appearance without adding extra HTML elements.

## 🧱 Technologies Used

- HTML5
- CSS3
- CSS Pseudo-elements
- Box-sizing
- Float and Positioning
- Media Queries

## 🎯 Key Concepts Practiced

Box Sizing Reset: The box-sizing: border-box; rule ensures consistent element sizing.

Layout Structure:
- Main container (#piano)
- Keys wrapper (.keys)
- White keys (.key)
- Black keys created with (.black--key::after)

Pseudo-elements: The selector .key.black--key::after is used to visually generate black piano keys while keeping the HTML structure clean.

Responsive Design: Media queries adjust the layout across three breakpoints:
- Under 768px → Compact layout
- 769px to 1199px → Medium layout
- 1200px and above → Full layout

## 📱 Responsive Behavior

The piano adapts to different screen sizes by adjusting container width, keys wrapper width, and logo size. This ensures usability across desktop, tablet, and smaller devices.

## 🚀 What I Learned

- Creating complex UI visuals using pure CSS
- Structuring layouts with positioning and float
- Using pseudo-elements effectively
- Applying media queries for responsiveness

## 📂 Project Location

Responsive Web Design Certification/Labs/design-a-piano

## 🔗 Repository

https://github.com/Vanitsas/FreeCodeCamp-All