package com.example.myapplication;

import android.app.Activity;
import android.content.pm.PackageManager;
import android.database.Cursor;
import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.Manifest;
import androidx.annotation.NonNull;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import com.example.myapplication.R;
import android.provider.Telephony;
import android.widget.Toast;

public class MainActivity extends Activity {
    private static final int SMS_PERMISSION_REQUEST_CODE = 101;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Check for SMS permission
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.READ_SMS)
                != PackageManager.PERMISSION_GRANTED) {
            // Permission is not granted, request it
            ActivityCompat.requestPermissions(this,
                    new String[]{Manifest.permission.READ_SMS},
                    SMS_PERMISSION_REQUEST_CODE);
        } else {
            // Permission is already granted, proceed to load and display SMS messages
            loadAndDisplayMessages();
        }
    }

    private void loadAndDisplayMessages() {
        // Sample data for messages (replace with your own data)
        String[] messages = {
                "Message 1: Is this a spam?",
                "Message 2: Is this a spam?",
                "Message 3: Is this a spam?"

        };

        // Retrieve SMS messages from the device
        Cursor cursor = getContentResolver().query(
                Telephony.Sms.Inbox.CONTENT_URI,  // SMS inbox content URI
                new String[]{Telephony.Sms.Inbox.BODY}, // Columns to retrieve (only the message body)
                null,
                null,
                null
        );

        if (cursor != null && cursor.moveToFirst()) {
            do {
                // Get the message body from the cursor
                String messageBody = cursor.getString(cursor.getColumnIndexOrThrow("body"));
                messages = append(messages, messageBody); // Add the SMS message to the array
            } while (cursor.moveToNext());

            cursor.close();
        }

        // Create an ArrayAdapter to populate the ListView with messages
        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, messages);

        // Get the ListView and set the adapter
        ListView messageListView = findViewById(R.id.messageListView);
        messageListView.setAdapter(adapter);
    }

    // Helper function to append a new element to an array
    private String[] append(String[] array, String element) {
        String[] newArray = new String[array.length + 1];
        System.arraycopy(array, 0, newArray, 0, array.length);
        newArray[array.length] = element;
        return newArray;
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions,
                                           @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode == SMS_PERMISSION_REQUEST_CODE) {
            if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                // Permission granted, proceed to load and display SMS messages
                loadAndDisplayMessages();
            } else {
                // Permission denied, show a message or handle it accordingly
                Toast.makeText(this, "SMS permission denied", Toast.LENGTH_SHORT).show();
            }
        }
    }
}
