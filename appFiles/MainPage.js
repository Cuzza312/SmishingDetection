import React, { useEffect, useState } from 'react';
import { View, Text, ScrollView, StyleSheet } from 'react-native';
import SmsListener from 'react-native-android-sms-listener';
import * as Permissions from 'expo-permissions';
import * as SMS from 'expo-sms';

const MainPage = () => {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    async function requestSmsPermission() {
      const { status } = await Permissions.askAsync(Permissions.SMS);
      if (status === 'granted') {
        // Permission granted, you can now access SMS messages
        initSmsListener();
      } else {
        // Permission denied, handle it gracefully
        console.error('SMS permission denied');
      }
    }

    async function initSmsListener() {
      // Initialize the SMS listener
      const listener = SmsListener.addListener((message) => {
        // Handle incoming message
        setMessages((prevMessages) => [...prevMessages, message]);
      });

      // Clean up the listener when the component unmounts
      return () => {
        listener.remove();
      };
    }

    // Request SMS permissions and initialize SMS listener when the component mounts
    requestSmsPermission();
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.heading}>SMS Messages</Text>
      <ScrollView style={styles.messageContainer}>
        {messages.map((message, index) => (
          <View key={index} style={styles.message}>
            <Text>{`From: ${message.address}`}</Text>
            <Text>{`Message: ${message.body}`}</Text>
          </View>
        ))}
      </ScrollView>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
  },
  heading: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  messageContainer: {
    flex: 1,
    marginTop: 10,
  },
  message: {
    padding: 10,
    backgroundColor: '#f0f0f0',
    marginBottom: 10,
    borderRadius: 5,
  },
});

export default MainPage;
