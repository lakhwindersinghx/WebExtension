import { startWebsiteTracking } from "./watchers/activityWatcher.js";
import { startAFKWatcher } from "./watchers/afkWatcher.js"
startWebsiteTracking();
startAFKWatcher();
