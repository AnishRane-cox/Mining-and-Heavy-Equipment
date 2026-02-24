# Fuel Consumption Prediction For Construction machinary using diesel engine 

## 1. Problem Statement

What problem?
This project aims to predict fuel consumption based on vehicle, engine displacemnt capacity, power, human, enviormental and sesonal conditions 

Why important?
Accurate predictions helps in measuraing the running cost of the vehicle and the fuel consumption of a vehcial on the basis of Ton\km\L.
Helps in predicting the sesonaly impact of the running cost of vehicals in harsh enviorments

Who benefits?
Provides an advantage to inhance the fleet returns and the output of the overall vehicle
selecting the right vehicle for the applications

## 2. Dataset
Real-time driving data and road environment data set of unmanned control system in open-pit coal mine. The data set can be used for fuel consumption prediction and unmanned truck scheduling.
Source - [A Dataset for Fuel Consumption Prediction in Driverless Mining Trucks Using Deep Siamese Transformer Networks - Figshare](https://figshare.com/s/7e6f90fc08adc113f7a7?utm_source=copilot.com&file=54669416)

Sample Size - 292 observations

Understanding the Data
Column Header	Meaning	How It’s Useful for Regression
date	The day the data was recorded	Helps track seasonal or temporal effects
vehicle model	Type of truck (CAT, Komatsu, Volvo, etc.)	Allows comparison across OEMs
Mileage (km)	Total distance travelled	Independent variable (X)
Actual fueling quantity (L)	Liters of fuel refilled	Can be used to validate consumption
Average temperature (°F)	Mean ambient temperature during operation	Environmental factor affecting fuel burn
Average wind speed (knots)	Mean wind speed	Impacts resistance and fuel use
Maximum temperature (°F)	Highest temperature recorded	Useful for stress/load conditions
Minimum temperature (°F)	Lowest temperature recorded	Same as above, for range analysis
Precipitation (in)	Rainfall during operation	Affects road condition and rolling resistance
road quality	Encoded measure of road condition (good, poor, rough)	Terrain factor
shift work	Day/night shift indicator	Operator behavior and visibility impact
Raise height difference	Elevation change in haul road	Directly affects fuel consumption
Width of working flat	Width of the haul road or working area	Impacts maneuvering and cycle time

Target - Ton-kilometer fuel consumption (L/km/t)	Fuel used per ton of material moved per kilometer

After looking into the data the data had the consideration of the vehiclae modle which didn’t provide a lot of insight about the engine thus we extended the data to also include the the engine specification for a scalable Model

Engine Specification for Vehicle model
Vehicle Model	RTH136	MT96	SKT105E
Engine Model	YCK16775-T300	WP13G530E310	WP13G530E310
Engine power (HP)	764	523	523
Engine size (L)	15.93	12.54	12.54
Vehicle weight (kg)	48000	33000	38000
Transmission type	Automatic	Automatic	Automatic
Fuel Type	Diesel	Diesel	Diesel
Numbers of cylinder	6	6	6
Load Capacity	100000	65000	70000

Data present in the database 
RangeIndex: 292 entries, 0 to 291
Data columns (total 20 columns):
 #   Column                                     Non-Null Count  Dtype         
---  ------                                     --------------  -----         
 0   date                                       292 non-null    datetime64[ns]
 1   Ton-kilometer fuel consumption L / km / t  292 non-null    float64       
 2   Mileage km                                 132 non-null    float64       
 3   Actual fueling quantity L                  150 non-null    float64       
 4   Average temperature ( ° F )                292 non-null    float64       
 5   Average wind speed ( knots )               292 non-null    float64       
 6   Maximum temperature ( ° F )                292 non-null    float64       
 7   Minimum temperature ( ° F )                292 non-null    float64       
 8   Precipitation ( in )                       292 non-null    float64       
 9   road quality                               292 non-null    float64       
 10  shift work                                 292 non-null    object        
 11  Raise height difference                    292 non-null    float64       
 12  Width of working flat                      292 non-null    float64       
 13  Engine power (HP)                          292 non-null    float64       
 14  Engine size (L)                            292 non-null    float64       
 15  Vehicle weight (kg)                        292 non-null    float64       
 16  Transmission type                          292 non-null    object        
 17  Fuel Type                                  292 non-null    object        
 18  Numbers of cylinder                        292 non-null    float64       
 19  Load Capacity                              292 non-null    float64       
dtypes: datetime64[ns](1), float64(16), object(3)
memory usage: 45.8+ KB

## 3. Methodology

1. Data Preprocessing 

## 4. Model Architecture

## 5. Installation

## 6. Usage

## 7. Results

## 8. Evaluation Metrics

## 9. Project Structure

## 10. Future Improvements

## 11. Author