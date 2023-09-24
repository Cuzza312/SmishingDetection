# SmishingDetection

## Running a React Native App - Setup and Requirements
### Prerequisites

1. **Node.js and npm:**
   - Download and install Node.js from [nodejs.org](https://nodejs.org/).
   - Verify the installation:
     ```bash
     node -v
     npm -v
     ```

2. **Java Development Kit (JDK):**
   - Install JDK 8 or later.
   - Verify the installation:
     ```bash
     java -version
     ```

3. **Android Studio (for Android development):**
   - Download and install Android Studio from [developer.android.com/studio](https://developer.android.com/studio).
   - During installation, ensure to install the Android SDK and necessary components.

4. **Xcode (for iOS development, Mac only):**
   - For macOS users, install Xcode from the Mac App Store.
   - Install Xcode Command Line Tools from Xcode preferences.

### React Native CLI

Install the React Native CLI globally:

```bash
npm install -g react-native-cli
```

### Running the app
1. You can use terminal VS code(recommended) or powershell, etc to CD into a folder or location of your choosing to make your app
   -  Then follow this quickstart instructions to setup your app and respond to the questions in the cli (https://reactnative.dev/docs/environment-setup?guide=quickstart)
   ```bash
   -npx create-expo-app AwesomeProject
   -cd AwesomeProject
   -npx expo start
   ```
_**IMPORTANT!**_
**_To run the smishing app_**
-  Download the repo - to be continued
-  install below dependencies before starting with a reset cache_.**
```bash
 -npm install @react-navigation/native
 -npm install @react-navigation/stack
 -npm start -- --reset-cache
```
