# Terminal (`p-terminal`)

**Import:**

```ts
import { TerminalModule } from "primeng/terminal";
```

## Example

```typescript
import { Component } from "@angular/core";
import { TerminalModule } from "primeng/terminal";

@Component({
  template: `
    <div class="card">
      <p>
        Enter "<strong>date</strong>" to display the current date, "<strong
          >greet &#123;0&#125;</strong
        >" for a message and "<strong>random</strong>" to get a random number.
      </p>
      <p-terminal welcomeMessage="Welcome to PrimeNG" prompt="primeng $" />
    </div>
  `,
  standalone: true,
  imports: [TerminalModule],
})
export class TerminalBasicDemo {
  subscription: Subscription;

  constructor() {
    this.subscription = this.terminalService.commandHandler.subscribe(
      (text) => {
        let response;
        let argsIndex = text.indexOf(" ");
        let command = argsIndex !== -1 ? text.substring(0, argsIndex) : text;
        switch (command) {
          case "date":
            response = "Today is " + new Date().toDateString();
            break;
          case "greet":
            response = "Hola " + text.substring(argsIndex + 1);
            break;
          case "random":
            response = Math.floor(Math.random() * 100);
            break;
          default:
            response = "Unknown command: " + command;
        }
        this.terminalService.sendResponse(response);
      },
    );
  }

  ngOnDestroy() {
    if (this.subscription) {
      this.subscription.unsubscribe();
    }
  }
}
```

## Inputs

| Name           | Type   | Default | Description                          |
| -------------- | ------ | ------- | ------------------------------------ |
| welcomeMessage | string | -       | Initial text to display on terminal. |
| prompt         | string | -       | Prompt text for each command.        |

**Full API & more examples:** https://primeng.org/terminal
