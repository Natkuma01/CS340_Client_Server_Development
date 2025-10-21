# Animal Rescue Finder Dashboard 🐶🐱

### Project Overview
The project is developed for an innovative international rescue animal training company – Grazioso Salvare. The data is provided by five non-profit shelters in the Austin, Texas region. This project creates a dashboard to view, filter, and analyze data with a pie chart, and see visual updates through a geolocation map that responds to selected filters.

<br>

### Required Functionally ⚙️
1. Users can filter animals by rescue type: 
* Water Rescue
* Mountain or Wilderness Rescue
* Disaster or Individual Tracking
* Reset
2. Data Table
* Displays filtered animal data directly from MongoDB database
* Supports column sorting and live filtering
3. Responsive Chart and Map
* Geolocation Map shows animal location dynamically
* Pie Chart shows the top 10 breeds within the current filter selection
4. Branding
* Add Grazioso Salvare logo on top of the page

<br>

### Screenshots 🩻
Initial Dashboard View (Unfiltered): 
<br>
<img width="524" height="273" alt="image" src="https://github.com/user-attachments/assets/8f9371f6-5f73-499e-9893-9cb245112527" />
<br>


Filtered for Disaster or Individual Tracking:
<br>
<img width="1087" height="447" alt="Screenshot 2025-10-21 at 5 39 58 PM" src="https://github.com/user-attachments/assets/3ddd6736-9777-4543-a312-260392c3720f" />
<br>

Pie chart:
<br>
<img width="600" height="280" alt="Screenshot 2025-10-21 at 5 41 11 PM" src="https://github.com/user-attachments/assets/178619c1-dcd8-4b1c-839d-8207da9312b8" />
<br>

### Tools and Technologies 🪛
Language: **Python** – core programming and logic<br>
Database: **MongoDB** – stores and retrieves animal records<br>
Framework: **Dash** – builds interactive web dashboards<br>
Data Handling: **Pandas** – cleans and manipulates data<br>
Visualization: **Plotly Express** – creates dynamic pie chart<br>
Mapping: **Leaflet** – displays animal locations on a map

<br>

### Why MongoDB? 
* MongoDB is highly flexible and strongly integrates with Python
* Stores animal data in JSON-like documents, ideal for different field types
* Integrates seamlessly with Python via the pymongo library
* Allow efficient querying and filtering on dashboard
* Converts easily to pandas DataFrames for visualization
<br>

### Why Dash Framework? <br>
* Allows lightweight full-stack web app creation with Python only
* Integrates directly with Plotly for interactive visualization
* Provides ready-to-use UI components such as radio items and data tables
* Support callback functions for creating a responsive user experience

### Project Steps 
1. Connected MongoDB database using a custom CRUD Python Module
2. Retrieved data from the “aac” collection with the read() method
3. Cleaned and formatted the retrieved records using pandas
4. Removed the “_id” fields for better visualization
5. Added logo, title, and creator information at the top of the dashboard
6. Implement a consistent layout with Dash’s HTML components
7. Added radio buttons, sorting, pagination, and the filter feature
8. Create a pie chart and a map visualization side-by-side
9. Test all functionality
1. Capture screenshots for documentation

### Challenges 🚀
One of the biggest challenges was achieving a clean and balanced layout. While the logic and data queries were relatively straightforward, the styling process took significant time and experimentation. Even though some layout code was provided, getting the map and pie chart to properly align side by side didn’t go as smoothly as expected. At first, the components kept overlapping or appearing misaligned. It took many rounds of trial and error, tweaking widths, adjusting padding, and refining the layout structure, before everything displayed neatly and proportionally. Another challenge I ran into was capturing clear screenshots of the dashboard. By default, when running the app in Jupyter, the output appears in a small, scrollable box, which made it difficult to take screenshots that clearly showed the charts and tables. To solve this, I researched online and discovered that I could run the dashboard in external mode and specify a custom port. This allowed me to open the dashboard in a full browser window, providing a larger, more readable view for screenshots. It made the documentation much cleaner and ensured that all elements, including the map and charts, were fully visible.

<br>

---

<br>

1. *How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?* <br>

I focus on clear structure, meaningful variable names, and good documentation. For example, in my CRUD Python module, each method was separated and had comments explaining what it did. This made it easy to reuse the same module later in Project Two, where I connected the dashboard to MongoDB. In the future, this same module could be reused for any project that needs a MongoDB connection, just by changing the collection or database name.

2. *How do you approach a problem as a computer scientist?* <br>
I approach problems by breaking them into smaller, manageable parts. First, I try to understand the problem fully. Then, I make a plan for solving it, deciding which steps or methods to use. Once I’m confident the plan will work, I start putting it into action.

3. *What do computer scientists do, and why does it matter?* <br>
I believe computer scientists solve real-world problems by designing systems that make data more useful and accessible. In this project, I built a dashboard that helps Grazioso Salvare analyze rescue animal data more efficiently. Instead of going through spreadsheets manually, users can now filter animals, see trends through a pie chart, and view rescue locations on a live map. 


