import React from "react";
import ReactDOM from "react-dom";
import { App, AppConfigProvider } from "@councildataproject/cdp-frontend";

import "@councildataproject/cdp-frontend/dist/index.css";

const config = {
    firebaseConfig: {
        options: {
            projectId: "cdp-colorado-school-boards-zfi",
        },
        settings: {},
    },
    municipality: {
        name: "Colorado School Boards",
        timeZone: "America/Denver",
        footerLinksSections: [],
    },
    features: {
        // enableClipping: false,
    },
}

ReactDOM.render(
    <div>
        <AppConfigProvider appConfig={config}>
            <App />
        </AppConfigProvider>
    </div>,
    document.getElementById("root")
);