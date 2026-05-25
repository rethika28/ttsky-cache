/*
 * Simple Cache Memory
 * TinyTapeout Compatible
 */

`default_nettype none

module tt_um_example (
    input  wire [7:0] ui_in,     
    output wire [7:0] uo_out,    

    input  wire [7:0] uio_in,    
    output wire [7:0] uio_out,   
    output wire [7:0] uio_oe,    

    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    //--------------------------------------------------
    // Input Mapping
    //--------------------------------------------------
    // ui_in[1:0] -> address
    // ui_in[7:2] -> write data
    // uio_in[0] -> write enable
    //--------------------------------------------------

    wire [1:0] addr;
    wire [5:0] write_data;
    wire       we;

    assign addr       = ui_in[1:0];
    assign write_data = ui_in[7:2];
    assign we         = uio_in[0];

    //--------------------------------------------------
    // Cache Memory
    //--------------------------------------------------

    reg [5:0] cache_mem [0:3];

    integer i;

    //--------------------------------------------------
    // Reset + Write Logic
    //--------------------------------------------------

    always @(posedge clk or negedge rst_n)
    begin
        if(!rst_n)
        begin
            for(i=0; i<4; i=i+1)
                cache_mem[i] <= 6'b000000;
        end

        else if(we)
        begin
            cache_mem[addr] <= write_data;
        end
    end

    //--------------------------------------------------
    // Read Logic
    //--------------------------------------------------

    wire [5:0] read_data;

    assign read_data = cache_mem[addr];

    //--------------------------------------------------
    // Output
    //--------------------------------------------------

    assign uo_out = {2'b00, read_data};

    //--------------------------------------------------
    // Unused IO
    //--------------------------------------------------

    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    //--------------------------------------------------
    // Prevent Warnings
    //--------------------------------------------------

    wire _unused = &{ena, uio_in[7:1], 1'b0};

endmodule
