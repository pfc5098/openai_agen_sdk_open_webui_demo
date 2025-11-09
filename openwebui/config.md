# Open WebUI Configuration  

To connect Open WebUI to this backend, add a custom model entry in Open WebUI's settings:  

1. Open the Models page in Open WebUI and click **Add custom model**.  
2. Set **Name** to `AgentSDK` (or any label you prefer).  
3. Set **Base URL** to `http://localhost:8000`.  
4. Set **API Path** to `/chat`.  
5. Enable **Streaming** so responses stream token by token.  
6. Save the model.  

You can now select this custom model in your Open WebUI chat interface to interact with the Agent running on this backend.
