```markdown
# WiFi Check

The `wifi_check.py` script is designed to monitor the status of a WiFi connection and automatically restart the wireless interface (`wlan0`) if the default gateway becomes unreachable. This can be especially useful in situations where maintaining a stable WiFi connection is crucial, and automatic recovery is desired when connectivity issues arise.

## Usage

Run the script using the following command:

```bash
python3 wifi_check.py [--force]
```

- `--force`: (Optional) Force restart the `wlan0` interface regardless of the connection status.

The script will continuously monitor the default gateway's reachability and take action accordingly. If the gateway is unreachable, the script will restart the wireless interface and log the action with a timestamp.

## Use Cases

1. **Remote IoT Devices**: When deployed on remote IoT devices, this script can help maintain a reliable WiFi connection. If the connection drops due to environmental factors or interference, the script will automatically attempt to restore the connection.

2. **Unattended Systems**: Systems that require unattended operation, such as headless servers or monitoring devices, can benefit from this script. It ensures that connectivity issues are resolved without manual intervention.

3. **Critical Infrastructure**: In scenarios where maintaining a stable network connection is critical (e.g., remote surveillance systems, data logging), the script helps ensure continuous operation.

4. **Development and Testing**: The `--force` flag allows developers to manually trigger a `wlan0` restart for testing and debugging purposes.

## Configuration

You can modify the script to change the monitoring interval, customize log messages, or adjust other parameters to fit your specific use case.

## Contributing

Contributions, bug reports, and feature requests are welcome! Feel free to fork this repository, make changes, and submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
```
