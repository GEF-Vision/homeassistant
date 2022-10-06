# Home Assistant Integration for GEF Vision

This integration allows fetching data from GEF Vision to Home Assistant.

## Installation
Easiest way to install the integration is using HACS. Information about HACS and it's installation can be found [here](https://hacs.xyz/)

Repository structure allows you to use the Custom Repositories -function in HACS. See [https://hacs.xyz/docs/faq/custom_repositories/](https://hacs.xyz/docs/faq/custom_repositories/) on how to install this integration.

After the integration has been installed (and Home Assistant restarted), the integration can be found with the name *GEF Vision*

## Required data in config flow
- Username: GEF Vision Username
- Password: GEF Vision Password
- Plant UUID: Unique id for the plant. Can be obtained from the monitoring URL.
- Poll interval: Data update interval in seconds. Default is 30 seconds, minimum is 10 seconds.

## Disclaimer
This integration is in active development and still work-in-progress. Breaking changes may occur. Use at your own risk!

## Support
If you have any problems with the integration or you find a bug, please open an issue to GitHub or send an e-mail to [tuki@gef.fi](tuki@gef.fi)
